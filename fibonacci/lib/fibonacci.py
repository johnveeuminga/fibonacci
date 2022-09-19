from fibonacci.models import FibonacciResult
from ..celery import app

@app.task
def create_fibonacci(n):
  val = calculate_fibonacci(n)
  res = FibonacciResult(id=n, value=val)  
  res.save()

  return val

def calculate_fibonacci(n):
  a = 0
  b = 1

  for i in range(2, n+1):
    c = a + b
    a = b
    b = c

  return b