import matplotlib.pyplot as plt
import time
from func import midPoint

def generateBezier(x1, x2, x3, y1, y2, y3, currIteration):
    if (currIteration < iteration):
        xMidLeft, yMidLeft = midPoint(x1, x2, y1, y2)
        xMidRight, yMidRight = midPoint(x2, x3, y2, y3)
        xMidMid, yMidMid = midPoint(xMidLeft, xMidRight, yMidLeft, yMidRight)
        currIteration = currIteration + 1
        generateBezier(x1, xMidLeft, xMidMid, y1, yMidLeft, yMidMid,  currIteration)
        x.append(xMidMid)
        y.append(yMidMid)
        generateBezier(xMidMid, xMidRight, x3, yMidMid, yMidRight, y3, currIteration)

x = []
y = []
        
print("====KURVA BEZIER====")

print("TITIK KONTROL ke - 1")
print("X")
abs = int(input("=> "))
x.append(abs)
print("Y")
oor = int(input("=> "))
y.append(oor)

print("TITIK KONTROL ke - 2")
print("X")
xCon = int(input("=> "))
print("Y")
yCon = int(input("=> "))

print("TITIK KONTROL ke - 3")
print("X")
xCon2 = int(input("=> "))
print("Y")
yCon2 = int(input("=> "))

print("ITERASI")
iteration = int(input("=> "))

start = time.time()

generateBezier(x[0], xCon, xCon2, y[0], yCon, yCon2, 0)

x.append(xCon2)
y.append(yCon2)

end = time.time()

print(end - start, 'ms')

ax = plt.subplot()
ax.plot(x, y, color = 'blue', linestyle = 'solid', linewidth = 2, marker = 'o', markersize = 5, markerfacecolor = 'black', markeredgecolor = 'black')
plt.title(f"Divide and Conquer dengan {iteration} iterasi")
plt.show()