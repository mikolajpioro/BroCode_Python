num = 5
a = 6
b = 7
# age = int(input("Enter your age: "))
# temperature = float(input("Enter the temperature: "))
password = "dupa"
entered_password = input("Enter the password: ")
user_role = "Admin" if entered_password == "dupa" else "User"

#print("Positive" if num > 0 else "Negative")
#result = "Even" if num % 2== 0 else "Odd"
# max_num = a if a > b else b
# min_num = a if a < b else b
# print(max_num)
# print(min_num)
# status = "Adult" if age >= 18 else "Minor"
# print(status)
# weather = "Hot" if temperature > 20 else "Cold"
# print(weather)
access_level = "Full access" if user_role == "Admin" else "Limited access"
print(access_level)