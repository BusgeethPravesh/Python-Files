"""Write a simple program that will prompt user to input a sentence.
Your program will count all lower case alphabets, upper case alphabets, digits, and special symbols.
Then your program will display the all the counts on screen."""

Sentence = input("Enter your sentence:")

upper = 0
lower = 0
number = 0
special = 0

for x in Sentence:

    if x.upper()>= 'A' and x <= 'Z':
            upper += 1
    elif x.lower() >= 'a' and x <= 'z':
            lower += 1
    elif x.isdigit():
            number += 1
    else:
            special += 1

print('Upper case letters:', upper)
print('Lower case letters:', lower)
print('Number:', number)
print('Special characters:', special)

