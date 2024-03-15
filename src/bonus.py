import matplotlib.pyplot as plt
import time
from func import *

x = []
y = []

print("====KURVA BEZIER====")

print("DERAJAT")
deg = int(input("=> "))

for i in range (deg+1):
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

for i in range (0, iteration): 
    
    xRes, yRes = generateBezier(x, y)
    x, y = xRes, yRes

    ax = plt.subplot()
    ax.plot(x, y, color = 'blue', linestyle = 'solid', linewidth = 2, marker = 'o', markersize = 5, markerfacecolor = 'red', markeredgecolor = 'none')
    plt.title(f"Iterasi ke - {i+1}")
    plt.show()

end = time.time()

print(end - start, 'ms')

