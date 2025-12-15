def calculate_factorial(n):
  """Calculates the factorial of a non-negative integer n."""
  if n < 0:
    return "Factorial is not defined for negative numbers"
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

# Example usage:
number = 5
print(f"The factorial of {number} is: {calculate_factorial(number)}")

# Using the math module
import math
print(f"The factorial of {number} using math.factorial is: {math.factorial(number)}")
