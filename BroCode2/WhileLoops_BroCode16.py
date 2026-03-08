# food = input("Enter a food you like: ")
#
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
#
# print("Bye")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")
