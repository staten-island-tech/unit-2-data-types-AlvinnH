import random

number_list = ["1", "2","3","4","5","6","7","8","9","10"]
random_number = random.choice(number_list)
wrong_list = []
correct = False
while correct == False:
    guess = input("Guess a number from 1-10 ")
    if guess == random_number:
        print("You have guessed correctly")
        print(wrong_list)
        correct = True
    elif guess != random_number:
        wrong_list.append(guess)
        print(wrong_list)
        if guess > random_number:
            print("The number is smaller than the one you guessed")
        elif guess < random_number:
            print("The number is bigger than the one you guessed")