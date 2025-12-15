def sum_arithmetic_progression(a, d, n):
  """
  Calculates the sum of an arithmetic progression.
  a: first term
  d: common difference
  n: number of terms
  """
  if n <= 0:
    return 0
  
  total_sum = (n / 2) * (2 * a + (n - 1) * d)
  return total_sum

# Example usage (AP: 2, 4, 6, 8, 10, ...):
first_term = 2
common_diff = 2
num_terms = 5
print(f"The sum of the first {num_terms} terms of the AP is: {sum_arithmetic_progression(first_term, common_diff, num_terms)}")