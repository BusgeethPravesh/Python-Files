"""Write a Python program for the stock of a pharmacy with menu
1. Add an item to stock pharmacy,
2. Remove item from stock,
3. Insert item at specified position.
Your program should do all the operations. """


list1=["Thermometer", "Hand sanitizer", "Lemsip", "Strepsils", "Pain Relief"]


count="yes"
while count.lower() == "yes":

    print("Stock of IOT Pharmacy:", list1)
    print("-To add an item, type '1'\n-To remove an item, type '2'\n-To insert an item, type '3'")

    decision = int(input("\nEnter your choice:"))

    if decision == 1:
        print(list1)
        x = input("Item to added:")
        list1.append(x)
        print(list1)
    elif decision == 2:
        print(list1)
        x = input("Item to be removed:")
        if x in list1:
            list1.remove(x)
            print(list1)
        else:
            print("Item not found.")
    elif decision == 3:
        print(list1)
        x = input("Enter item to be inserted:")
        y = int(input("Enter the index to insert the item:"))
        if y < len(list1):
            list1.insert(y, x)
            print(list1)
        else:
            print("Invalid Position.")
    else:
        print("Invalid input.")

    count = input("\nContinue? Yes/No?")
    if count == " no ":
        break

