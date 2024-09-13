import random
computer = random.choice([1,-1,0])
num=input("enter your choice: ")
Dict = {"s": 1, "w": -1, "g": 0}
rvsDict={1: "Snake", -1: "Water", 0: "Gun"}
you=Dict[num]
print(f"You chose {rvsDict[you]}\nComputer chose {rvsDict[computer]}")

if computer == you:
    print("Draw")
else:
    if(computer==-1 and you==1):
        print("You Win!")

    elif(computer==1 and you == -1):
        print("computer Win!")

    elif(computer==-1 and you ==0):
        print("Computer win!")

    elif(computer == 0 and you == -1):
        print("you Win!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif computer == 0 and you == 1:
        print("Computer Win!")