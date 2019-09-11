"""Write a Python program that will accept four lists of four values.
Then your program should find the list whose sum of elements is the highest and display the list."""

#create list and find sum
count=0
total_1=0
list1=[]
print("\nLIST 1:")
while count<=3:
    addintegers=int(input("Enter integer:"))
    list1.append(addintegers)
    count+=1
for addintegers in list1:
    total_1 =(total_1+addintegers)

print("Total for List 1:",total_1)

#create list2 and find sum
count=0
total_2=0
list2=[]
print("\nLIST 2:")
while count<=3:
    addintegers=int(input("Enter integer:"))
    list2.append(addintegers)
    count+=1
for addintegers in list2:
    total_2 =(total_2+addintegers)

print("Total for List 2:",total_2)

#create list3 and find sum
count=0
total_3=0
list3=[]
print("\nLIST 3:")
while count<=3:
    addintegers=int(input("Enter integer:"))
    list3.append(addintegers)
    count+=1
for addintegers in list3:
    total_3 =(total_3+addintegers)

print("Total for List 3:",total_3)

#create list4 and find sum
count=0
total_4=0
list4=[]
print("\nLIST 4:")
while count<=3:
    addintegers=int(input("Enter integer:"))
    list4.append(addintegers)
    count+=1
for addintegers in list4:
    total_4 =(total_4+addintegers)

print("\nTotal for List 1:",total_1)
print("Total for List 2:",total_2)
print("Total for List 3:",total_3)
print("Total for List 4:",total_4)

#finding the highest total and display the list
if total_1 > (total_2 and total_3 and total_4):
    print("\nThe highest sum is in List 1:" , list1, "\nThe sum is:", total_1)
elif total_2 >(total_1 and total_3 and total_4):
    print("\nThe highest sum is in List 2:", list2, "\nThe sum is:", total_2)
elif total_3 >(total_1 and total_2 and total_4):
    print("\nThe highest sum is in List 3:", list3, "\nThe sum is:", total_3)
elif total_4>(total_1 and total_2 and total_3):
    print("\nThe highest sum is in List 4:", list4, "\nThe sum is:", total_4)


