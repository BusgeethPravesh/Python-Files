"""Write a Python program that will accept a number. If you reverse the given number
and it is the same as the original number then the program should return true"""

num1 = int(input("Enter number: "))

def reverse(num1):
    rev = 0
    while (num1 > 0):
        x = (num1%10)
        rev=(rev*10+x)
        num1=(num1//10)
    return rev

z = reverse(num1)

print("Reverse of the number:", z)

if num1 == z:
    print("TRUE.")
else:
    print("FALSE.")