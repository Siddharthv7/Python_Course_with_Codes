a = int(input("Enter you age:"))

# If statement no: 1
if(a%2 == 0):
    print("a is even")
# End of statement no: 1
    
#if statement no: 2
if(a>=18):
    print("You are above the age of consent")
    
elif(a<0):
    print("you are entering an invaild nagative age")
elif(a==0):
    print("you are enter 0")
else:
    print("you are below the age of consent")
    
print("End of program")