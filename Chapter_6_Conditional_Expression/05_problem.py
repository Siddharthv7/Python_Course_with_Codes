a1 = int(input("Enter suject marks 1: "))
a2 = int(input("Enter suject marks 2: "))
a3 = int(input("Enter suject marks 3: "))

# check for total percentage
total_percentage = (100*(a1 + a2 + a3))/300

if(total_percentage>=40 and a1>=33 and a2>=33 and a3>=33):
    print("your are pass", total_percentage)
else:
    ("you are fail", total_percentage)