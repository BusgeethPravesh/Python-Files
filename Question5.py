"""Write a Python program that will find the H.C.F of two input number."""

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if a>b:
    max1 = b
else:
    max1 = a

for i in range(1,max1+1):
    if (a% i == 0) and (b % i == 0):
        hcf = i
print(hcf)