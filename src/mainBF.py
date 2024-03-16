import matplotlib.pyplot as plt
import time
from func import *

x = []
y = []

print("====KURVA BEZIER====")

for i in range (3):
    print(f"TITIK KONTROL ke - {i+1}")
    print("X")
    abs = int(input("=> "))
    x.append(abs)
    print("Y")
    oor = int(input("=> "))
    y.append(oor)

print("ITERASI")
iteration = int(input("=> "))

start = time.time()

for i in range (iteration): 
    
    xRes, yRes = generateBezier(x, y)
    x, y = xRes, yRes

xShow = []
yShow = []
for j in range (0, len(x), 2):
    xShow.append(x[j])
    yShow.append(y[j])

end = time.time()

print(end - start, 'ms')

ax = plt.subplot()
ax.plot(xShow, yShow, color = 'blue', linestyle = 'solid', linewidth = 2, marker = 'o', markersize = 5, markerfacecolor = 'black', markeredgecolor = 'black')
plt.title(f"Brute Force dengan {iteration} iterasi")
plt.show()