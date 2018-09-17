# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import random

number = random.randint(1, 100)
guess = 0
while True:
    num_input = input("input number:")
    guess += 1
    if not num_input.isdigit():
        print("input number:")
    elif int(num_input) < 0 or int(num_input) >= 100:
        print("must 1-100")
    else:
        if number == int(num_input):
            print("%d" % guess)
            break
        elif number > int(num_input):
            print("min")
        elif number < int(num_input):
            print("max")
        else:
            print("error")
