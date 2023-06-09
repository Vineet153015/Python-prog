import time

# waqt = time.strftime("%H:%M:%S")
# print("Time is :",waqt)
# hour= int(time.strftime("%H"))
# if hour >= int(5) and hour <= int(12):
#     print("Good Morning")
# elif hour >= int(12) and hour <= int(17):
#     print("Good Afternoon")
# else:
#     print("Good Evening")

# print(hour)

name = input("Enter your Name : ")
waqt2 =time.strftime("%H:%M:%S")
print("Time Is :",waqt2)
hrs = int(time.strftime("%H"))
Min=int(time.strftime("%M"))
sec=int(time.strftime("%S"))
if hrs >= int(5) and hrs <=int(11) and Min > int(00) and sec < int(59):
    print("Good Morning ",name)
elif hrs >= int(12) and hrs <= int(16) and Min > int(00) and sec < int(59):
    print("Good Afternoon ",name)
else:
    print("Good Evening" ,name)