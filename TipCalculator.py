bill = input("What is the bill?")
tips = input("How much do you want to tip? (0-1)")
total = int(float(bill) * float(tips)) + float(bill)
print(total)