# temp = 40
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor even is still scheduled")
temp = 25
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside ")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside ")
    print("It's sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside ")
    print("It's sunny")
elif temp <= 0 and not is_sunny:
    print("It is cold outside ")
    print("It's cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside ")
    print("It's cloudy")