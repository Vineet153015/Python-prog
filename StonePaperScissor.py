import random

comp = ['Stone','Scissors','Paper']
user = ['Stone','Scissors','Paper']

list1 = list(comp)

head = "Welcome to Stone Paper Scissors Python Game"
up = head.upper()
print(up.center(164,'-'))
ans = True
while ans:
    print("Select Your Choice")
    print('1: Stone')
    print("2: Scissors")
    print("3: Paper")
    choice = int(input("Your choice : "))

    rand = random.choice(list1)
    if choice == 1 and rand!=user[0] and rand!=user[2]:
        print("You won")
        print("Computer's choice is : ",rand)
        print("Your Choice is : ",user[0])
        print("Stone Crushes the Scissor , Wooooooooooo")
        print("\n")
        # exit()
    elif choice == 2 and rand!=user[0] and rand!=user[1]:
        print("You won")
        print("Computer's choice is : ",rand)
        print("Your Choice is : ",user[1])
        print("Scissor cuts the paper into pieces, Wooooooooooo")
        print("\n")
        # exit()
    elif choice == 3 and rand!=user[1] and rand!=user[2]:
        print("You won")
        print("Computer's choice is : ",rand)
        print("Your Choice is : ",user[2])
        print("Paper wraps the stone, Wooooooooooo")
        print("\n")
        # exit()
    elif choice==1 and rand==user[0]:
        print("Draw")
        print("Computer's choice is : ",rand)
        print("Your Choice is : ",user[0])
        print("No one Wins, Bruh")
        print("\n")
        # exit()
    elif choice==2 and rand==user[1]:
        print("Draw")
        print("Computer's choice is : ",rand)
        print("Your Choice is : ",user[1])
        print("No one Wins, Bruh")
        print("\n")
        # exit()
    elif choice==3 and rand==user[2]:
        print("Draw")
        print("Computer's choice is : ",rand)
        print("Your Choice is : ",user[2])
        print("No one Wins, Bruh")
        print("\n")
        # exit()
        
    else:
        print("You lost")
        print("Computer's choice is : ",rand)
        print("Your Choice is : ",user[choice-1])
        print("\n")
        exit()