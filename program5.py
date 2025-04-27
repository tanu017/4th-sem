def power_bruteforce(a, n):
  result = 1
  for i in range(n):
    result *= a
  return result

def power_divide_conquer(a, n):
  if n==0:
    return 1
  elif n%2==0:
    return power_divide_conquer(a*a, n//2)
  else: 
    return a * power_divide_conquer(a*a, n//2)

a, n = map(int, input("Enter the values of a and n: ").split())
result_BF = power_bruteforce(a, n)
result_DC = power_divide_conquer(a, n)
print("Result using Brute Force: ", result_BF)
print("Result using Divide and Conquer: ", result_DC)
