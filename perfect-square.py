import math

def is_perfect_square(number):
  """Checks if a number is a perfect square."""
  if number < 0:
    return False  # Negative numbers cannot be perfect squares
  sqrt_num = math.sqrt(number)
  return sqrt_num == int(sqrt_num)

# Example usage
print(is_perfect_square(9))  # Output: True
print(is_perfect_square(15))  # Output: False
