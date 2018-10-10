# This program adds even numbers upto the number specified by the user

n = int(input("Enter the number "))

sum = 0
i=0
while i<=n:
  sum = sum + i
  i=i+2

print("Sum is",sum)
