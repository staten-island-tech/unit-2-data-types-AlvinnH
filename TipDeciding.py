print("What is the bill? ")
bill = float(input())
print("Was the service bad, okay, good, or great?")
service = input()
if service == "bad":
    total = bill
    print(total)
elif service == "okay":
    total = float(bill * 1.15)
    print(total)
elif service == "good":
    total = float(bill * 1.2)
    print(total)
elif service == "great":
    total = float(bill * 1.25)
    print(total)
