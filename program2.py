import time 
import matplotlib.pyplot as plt
def binary_search(arr, low, high, key):
  while low<=high: 
    mid = (low+high)//2
    if arr[mid] == key: 
      return mid
    elif arr[mid] < key: 
      low = mid + 1
    else: 
      high = mid - 1
  return -1

def main():
  n_values = []
  times = []
  r = int(input("Enter the number of runs: "))
  for _ in range(r):
    n = int(input("Enter the number of elements: "))
    arr = sorted(list(map(int, input("Enter the elements of the array: ").split())))
    key = int(input("Enter the key element to be searched: "))
    repeat = 10000
    start = time.time()
    for _ in range(repeat):
      result = binary_search(arr, 0, n-1, key)
    end = time.time()
    if result != -1: 
      print(f"Key {key} found at position {result}")
    else: 
      print(f"Key {key} not found")
    time_taken = (end-start)*1000
    print(f"Time taken for searching an element = {time_taken} milliseconds")
    n_values.append(n)
    times.append(time_taken)
  plt.figure()
  plt.plot(n_values, times, 'o-')
  plt.xlabel("Number of elements(n)")
  plt.ylabel("Time taken(milliseconds)")
  plt.title("Binary search time complexity")
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  main()
