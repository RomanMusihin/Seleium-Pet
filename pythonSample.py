# print("Hello motherfucker")
# if 3+3 == 5:
#     print("Good job motherfucker")
# else:
#     print("You are wrong motherfucker")


shit_happens = True
user_data = int(input("Введи число: "))
if user_data == 5 and shit_happens:
    print(user_data, "равно пяти")
elif user_data > 5 and shit_happens:
    print(user_data, "больше пяти")
elif shit_happens:
    print(user_data, "меньше пяти")
else:
    print(user_data, "shit")

# shit_happens = False
# if not shit_happens:
#     print("You are naive")
# else:
#     print("You are realistic")