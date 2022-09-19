from venv import create
from rest_framework import status
from fibonacci.lib.fibonacci import create_fibonacci
from rest_framework.test import APITestCase


class FibonacciTestCase(APITestCase):
  def setUp(self):
    create_fibonacci(9) 

  def test_non_existing_value(self):
    n=12
    response = self.client.post('/fibonacci/', {'n': n}, format='json')
    content = response.json()
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(content['status'], 'calculating')
    self.assertEqual(content['nth'], None)

  def test_existing_value(self):
    n=9
    response = self.client.post('/fibonacci/', {'n': n}, format='json')
    content = response.json()
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(content['status'], 'success')
    self.assertEqual(content['nth'], 34)

  def test_invalid_input(self):
    n="2.3"
    response = self.client.post('/fibonacci/', {'n': n}, format='json')

    self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_negative_input(self):
    n=-23
    response = self.client.post('/fibonacci/', {'n': n}, format='json')

    self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
