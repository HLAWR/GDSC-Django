x=input("Please enter the pattern to be printed: ")
if(len(x)!=1):
    print("The length of the character should be 1.")
elif( x=='a'or x=='e'or x=='i'or x=='o'or x=='u'):
    print("Vowels are not allowed in the input.")
else:
    for i in range(5):
        k=2*i+1
        for j in range(k):
            
            print(x, end='')
        print('\n')
