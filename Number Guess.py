import random

number_list = ["1","2","3","4","5","6","7","8","9","10"]
random_number = random.choice(number_list)
wrong_list = []
correct = False
while correct == False:
    guess = input(random_number)
    if guess == random_number:
        print("You have guessed the number!")
        print(wrong_list)
        correct = True
    elif guess != random_number:
        wrong_list.append(guess)
print(wrong_list)
if guess > random_number:
    print("Your guess is greater than the random number")
elif guess < random_number:
    print("Your guess is lower than the random number")