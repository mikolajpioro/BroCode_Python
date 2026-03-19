fruits = ["apple", "orange", "coconut", "banana"]
vegetables = ["celery", "carrot", "tomato", "potato"]
meats = ["chicken", "fish" "turkey"]

groceries = [fruits, vegetables, meats]


# print(groceries[1][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()