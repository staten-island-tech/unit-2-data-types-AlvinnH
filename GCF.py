x = int(input('First Number: '))
y = int(input('Second Number: '))
def gcf(x,y):
    for i in range(1,x+1):
          if (x % i == 0) and (y % i == 0):
                gcf = i
    return(gcf)
print(gcf(x,y))
