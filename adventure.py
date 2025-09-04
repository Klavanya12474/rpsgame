name=input("Enter your name: ")
print("welcome to the game! ")
answer=input("you walk on a dirt road chose left or right(left/right)? ").lower()
if answer=="left":
    answer=input("you came to a river chose walk around the river or swim across the river(walk/swim)? ").lower()
    if answer=="swim":
        print("there is crocodile in river so you lost")
    elif answer=="walk":
        print("you walk for miles but you didn't reach the end so you lost")
    else:
        print("enter valid option")
elif answer=="right":
    answer=input("you reached the road and there is stranger there will you talk to the stranger(yes/no)?").lower()
    if answer=="yes":
        print("stranger gives you gold coins and you won the game")
    elif answer=="no":
        print("you lose gold coins")
    else:
        print("enter valid option")
else:
    print("enter valid option")
print("thanks for playing game "+ name)
