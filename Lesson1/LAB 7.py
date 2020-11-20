from random import randint

cash=int(input("A game costs 3$\nHow much money do you want to charge? \n"))
turns=cash//3
print("you have " + str(turns) + " games to play\n")
if(cash%3)!=0:
    print("your change is:" + str(cash%3) + "$\n")
print("$$$Welcome to the Dice Games$$$\n_______________________________\n")
for i in range(turns):
    roll=int(input("Press 1 to roll the dices:"))
    if roll==1:
        cube1 = randint(1, 6)
        cube2 = randint(1, 6)
        if (cube1==cube2) & (cube1+cube2!=6):
            print("\nCube1: " + str(cube1) + " Cube2: " + str(cube2) + "\nYou won 100$!!!\n_____")
        elif (cube1==cube2) & (cube1+cube2==6):
            print("\nCube1: " + str(cube1) + " Cube2: " + str(cube2) + "\nyou won 1000$!!!\n_____")
        elif (cube1!=cube2) & (cube2==2) & (cube1 != 1):
            print("\nCube1: " + str(cube1) + " Cube2: " + str(cube2) + "\nYou won 40$!!\n_____")
        elif (cube1!=cube2) & (cube1==1) & (cube2!=2):
            print("\nCube1: " + str(cube1) + " Cube2: " + str(cube2) + "\nYou won 20$!!\n_____")
        elif (cube1 == 1) & (cube2==2):
            print("\nCube1: " + str(cube1) + " Cube2: " + str(cube2) + "\nYou won 60$!!\n_____")
        else:
            print("\nCube1: " + str(cube1) + " Cube2: " + str(cube2) + "\nYou won nothing!\nTry again!\n_____")
    else:
        print("Press 1 to roll the dices!!!\n")
print("your game is over!\nsee you later!")