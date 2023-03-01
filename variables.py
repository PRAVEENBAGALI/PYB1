age = 10
height=160.2
com= 1+10j

base = int(input("Enter Base: "))
height = int(input("Enter Height: "))
print(f"Area of Triangle =",0.5*base*height)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x =2
y = (2*x)-2
print(f"Slope",y)

#Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
x1,x2 = 2,6
y1,y2 = 2,10
m = (y2-y1)/(x2-x1)
print(f"Solpe is:" ,m)

#########################################
year = int(input("Age in No of Years: "))
seconds = year * 365 * 24 * 60 * 60
print(f"No of Seconds lived", seconds)


###############################################

def seconds_lived(years):
    second = years * 365 * 24 * 60 * 60
    return second


print(f"No of Seconds lived", seconds_lived(50))


#################################################

def tables(row, col):
    num = 1
    for i in range(1, n):
        for j in range(1,):
            print(row + col)


print(tables(5, 5))
