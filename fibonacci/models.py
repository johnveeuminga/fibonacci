from django.db import models

class FibonacciResult(models.Model):
  id = models.BigIntegerField(primary_key=True)
  value = models.PositiveBigIntegerField()