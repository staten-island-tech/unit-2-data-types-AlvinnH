number = int(input("Enter a number: "))
print("The factors of {x} are: ")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
