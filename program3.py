def toh(n, source, temp, dest):
  global count
  if n>0:
    toh(n-1, source, dest, temp)
    print(f"Move disk {n}: {source} -> {dest}")
    count += 1
    toh(n-1, temp, source, dest)

source ='S'
dest = 'D'
temp ='T'
n = int(input("Enter the number of disks: "))
count = 0
toh(n, source, temp, dest)
print("The number of moves: ", count)
