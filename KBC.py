import random

welcome = "Welcome to kon banega crorepati"
title1 = welcome.upper()
print(title1.center(200,"-"))
print("\n")
print("INSTRUCTIONS")
print("\n")
instruction = "* You will get the question and for each correct answer\n* you will be rewarded with 2 crores of money reward\n* there will be 4 option\n* 10 sets of questions\n"
title2 = instruction.title()
print(title2)
print("\n")
wish = 'Best of luck :)'
print(wish.center(200,"-"))

money = 0

questions = ["Q: Current Railway Minister of India is:\nA:Mamta Banarjee            B:Ashwini Vaishnaw\nC:Ram Vilash                D:Piyush Goyal",
            "Q: Which god is also known as 'Gauri Nandan'?\nA:Agni            B:Hanuman\nC:Ganesha         D:Indra",
            "Q: What does not grow on tree according to a popular Hindi saying?\nA: Money            B:Fruits\nC:Leaves            D:Flowers",
            "Q: Which city is known as Pink City in India??\nA:Jaipur            B:Kochi\nC:Banglore          D:Maysore",
            "Q: Who wrote India's National Anthem?\nA:Chetan Bhagat            B:RK Narayan\nC:Lal Bahadur Shastri      D:Rabindranath Tagore",
            "Q: When is the National Hindi Diwas celebrated?\nA:15 August            B:14 July\nC:13 September          D:14 September ",
            "Q: How many states are there in India?\nA:31            B:29\nC:38          D:28",
            "Q: Where in India Gate located?\nA:New delhi            B:Mumbai\nC:Pune            D:Ghazibad"]
# print(questions[7])
# for i in range(0,11):
list1 = list(questions)
while len(list1)>0:
        random_que = random.choice(list1)
        print(random_que)
        list1.remove(random_que)
        if random_que==questions[0]:
            print("Enter your Choice:")
            ans = input(":")
            match ans:
                case "B":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()
        if random_que==questions[1]:
            print("Enter your Choice:")
            ans = input()
            match ans:
                case "C":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()
        if random_que==questions[2]:
            print("Enter your Choice:")
            ans = input()
            match ans:
                case "A":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()
        if random_que==questions[3]:
            print("Enter your Choice:")
            ans = input()
            match ans:
                case "A":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()
        if random_que==questions[4]:
            print("Enter your Choice:")
            ans = input()
            match ans:
                case "D":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()
        if random_que==questions[5]:
            print("Enter your Choice:")
            ans = input()
            match ans:
                case "D":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()
        if random_que==questions[6]:
            print("Enter your Choice:")
            ans = input()
            match ans:
                case "D":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()
        if random_que==questions[7]:
            print("Enter your Choice:")
            ans = input()
            match ans:
                case "A":
                    print("Correct answer, you won 2 crore")
                    money = money+2
                    print("Prize money Won :",money)
                    print("\n")
                
                case _:
                    print("Sorry Better luck next time")
                    print("Prize money Won :",money)
                    print("\n")
                    exit()

print("Thank you for playing KBC")
print("You won :",money,"Crores")