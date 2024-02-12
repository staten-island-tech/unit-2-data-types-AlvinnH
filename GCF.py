x = int(input('First Number'))
y = int(input('Second Number'))
def gcf(x,y):
    if x > y:
            smaller = y
    else:
          smaller = x
    for i in range(1,x+1):
          if (x % i == 0) and (y % i == 0):
                hcf = i
    return(hcf)
print(gcf(x,y))
