x = int(input("What is the base of the triangle?"))
while x > 10^6 or x < 1:
    print("Your value exceeds the limit! (1 <= base => 10^6)")
    x = int(input("What is the base of the triangle?"))
y = int(input("What is the area of the triangle?"))
while y > 10^6 or y < 1:
    print("Your value exceeds the limit! (1 <= base => 10^6)")
    y = int(input("What is the area of the triangle?"))
def triangle(x,y):
    for i in range(x+1):
          if (x*i) % 2 > y:
            print(f"There can be a triangle made with base:{x} and area:{y}")
            print(i)
print(triangle(x,y))