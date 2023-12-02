'''
the question doesn't state to list all the numbers but it states to print the even
numbers indirectly and to print even numbers that are multiple of 3 & 5 as 3 and 5 respectively.
# The program doesn't restrict any cases like 15 which is multiple of 3 & 5,
    so the program will use '3&5' for such numbers accordingly.
'''
five=0
three=0
sum=0
for i in range(1,51):
    if (i%2==0):
        sum+=i
        if (i%3==0 and i%5==0):
            print("3&5 ")
            three+=1
            five+=1
        elif (i%3==0):
            print(3, " ")
            three+=1
        elif (i%5==0):
            print(5, " ")
            five+=1
        else:
            print(i, " ")

print("three count: ", three)         
print("five count: ", five)        
print("sum: ", sum) 
