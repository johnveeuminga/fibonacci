from xmlrpc.client import ResponseError
from rest_framework import viewsets
from fibonacci.lib.fibonacci import create_fibonacci

from fibonacci.models import FibonacciResult
from fibonacci.serializers import FibonacciSerializer
from rest_framework.response import Response

class FibonacciViewSet(viewsets.ModelViewSet):
  queryset = FibonacciResult.objects.all().order_by('id')
  serializer_class = FibonacciSerializer

  def create(self, request):
    try:
      n = int(request.data['n'])
      if n < 0:
        # Checks for negative input
        return Response({
          'message': 'Invalid Input'
        }, 400)

      if n <= 1:
        # Since the start of the sequence is always [0, 1]
        # we just output the their input to save calculation time.
        return Response({
          'nth': n,
          'status': 'success'
        })

      # Checks if the nth number in the sequence is stored in the database.
      res = self.get_queryset().filter(pk=n)
      
      if res.exists():
        # If exists, return the value
        return Response({
          'nth': res.first().value,
          'status': 'success'
        })
      else:
        # Calcualte nth number on background
        create_fibonacci.delay(n)
        return Response({
          'nth': None,
          'status': 'calculating'
        })
    except ValueError:
      return Response({
        'message': 'Invalid Input'
      }, status=400)
    