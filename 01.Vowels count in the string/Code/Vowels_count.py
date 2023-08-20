#Python Program to Count the Number of Vowels in a String

mystring = input("Enter the string: ")

numberofvowels = []

for i in mystring:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        numberofvowels.append(i)
    else:
        pass
    
print(numberofvowels)
print(len(numberofvowels))
