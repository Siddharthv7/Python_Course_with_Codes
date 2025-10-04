'''
1 for sanke
-1 for water
0 for gun
'''
computer = -1
player = input("Enter your choice: ")
youDict = {"s": 1, "w": -1,"g": 0}
reverseDict = {1 : "Snake", -1 : "Water",0 : "Gun"}

you = youDict[player]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Draw!")
else:
    if (computer == -1 and you ==1):
        print("You win!")
    elif(computer ==-1 and you ==0):
        print("You lose!")
    elif(computer ==0 and you ==1):
        print("You lose!")
    elif(computer ==0 and you ==-1):
        print("You win!")
    elif(computer ==1 and you ==0):
        print("You win!")
    elif(computer ==1 and you ==-1):
        print("You lose!")
        
    else:
        print("Something went worng!")