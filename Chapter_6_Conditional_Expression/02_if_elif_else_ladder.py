a = int(input("Enter you age:"))

# If elif else ladder
if(a>=19):
    print("You are above the age of consent")
    
elif(a<0):
    print("you are entering an invaild nagative age")
elif(a==0):
    print("you are enter 0")
else:
    print("you are below the age of consent")
    
print("End of program")