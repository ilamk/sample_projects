"""Collatzs the input number recursively until the result reaches 1."""

def collatz(number):
  global result
  if number % 2 == 0:
    print(number, ' // 2')
    result = number // 2
    return result
  elif number % 2 == 1:
    print('3 * ', number, ' + 1')
    result = 3 * number + 1
    return result

while True:
  try:
    n = int(input('Enter a number: '))
  except:
    print("Try again")
    continue
  collatz(n)
  if result == 1:
    print('End')
    break
