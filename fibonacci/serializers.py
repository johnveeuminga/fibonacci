from rest_framework import serializers

from fibonacci.models import FibonacciResult

class FibonacciSerializer(serializers.ModelSerializer):
  class Meta:
    model = FibonacciResult
    fields = ['id', 'value']
