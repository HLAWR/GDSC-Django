print("Exercise 1: Create the world")
print("Hello, World!")

print("Exercise 2: Add")
x = int(input("Enter the number: "))
y = int(input("Enter the other number: "))
print("The sum of ",x," and ",y," is ",(x+y))

print("Exercise 3: -/0/+")
x=int(input("Enter the number: "))
if x>0:
    print(x," is positve number.")
elif x<0:
    print(x," is negative number.")
else:
    print("The number, ",x," is neither positive nor negative.")

print("Exercise 4: length of string")
value = input("Enter the string: ")
print("The length of the string is ", len(value))

print("Exercise 5: Add n number of integer lists")
num=0
n=int(input("Enter the amount of numbers to be entered: "))
for i in range(0,n):
    number=int(input("Number: "))
    num+=number
print("The sum of the numbers is ",num)

print("Exercise 6: Anagrams")
str1 = input("Enter string-1: ")
str2 = input("Enter string-2: ")
if (sorted(str1)==sorted(str2)):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

print("Exercise 7: Big and small")
import sys 
less = sys.maxsize
large = sys.float_info.min
n=int(input("Enter the amount of numbers to be entered: "))
for i in range(0,n):
    number=int(input("Number: "))
    if less > number:
        less = number
    if large < number:
        large = number
print("Largest: ",large,", Smallest: ",less)
    

