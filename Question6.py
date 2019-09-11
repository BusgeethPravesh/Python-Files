"""Write a Python program that will accept two lists of integer.
Your program should create a third list such that it contain only odd numbers
from the first list and even numbers from the second list."""

print("This Program will allow you to enter two list of 5 integers "
      "\nand will then print the odd numbers from list 1 and even numbers from list 2. ")

tryagain="yes"
while tryagain=="yes":
    count=0
    list1=[]
    print("\nLIST 1:")
    while count<=4:
        addintegers=input("Enter integer:")
        list1.append(addintegers)
        count+=1
    print("\nList 1:",list1)


    count=0
    list2=[]
    print("\nLIST 2:")
    while count<=4:
        addintegers=input("Enter integer:")
        list2.append(addintegers)
        count+=1

    print("\nList 1:",list1)
    print("List 2:",list2)


    even_numbers=[]
    odd_numbers=[]

    for addintegers in (list1):
        if int(addintegers)% 2 != 0:
            odd_numbers.append(addintegers)
        #else:
         #   print("No Odd Number in LIST 1")

    for addintegers in (list2):
        if int(addintegers) % 2 == 0:
            even_numbers.append(addintegers)
       # else:
        #    print("No Even Number in LIST 2")

   # print("\nOdd Numbers in List 1:", odd_numbers)
   # print("Even Numbers in List 2", even_numbers)

    print("\nOdd Numbers from List 1 and Even Numbers from List 2:",odd_numbers,even_numbers)

    tryagain = input("\nContinue? Yes/No?")
    if tryagain == " no ":
        break