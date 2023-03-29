from math import comb, floor, ceil
import matplotlib.pyplot as plt
import numpy as np

def fy(y, n, r):
    omega = comb(r, n)
    if y < n or y > r:
        return 0.0
    if y == n:
        return 1/omega
    if (n+1) <= y and y <= r:
        return comb(y, n)/omega - comb(y-1, n)/omega

def Fy(y, n, r):
    if floor(y) < n:
        return 0

    if n <= floor(y) and floor(y) <= r:
        return comb(floor(y),n)/comb(floor(r),n)

    return 1.0

def Ey(n: int, r: int, funct: callable):
    esp = 0
    for y in range(n,r+1):
        esp += y*funct(y, n, r)

    return esp


def fz(z: int, n: int , r: int):
    if 1 <= z and z <= r-n:
        return comb(r-z+1, n)/comb(r, n) - comb(r-z, n)/comb(r, n)
    if z == r - n +1:
        return 1 / comb(r, n)

    return 0.0

def Fz(z, n, r):
    if floor(z) < 1:
        return 0

    if 1 <= floor(z) and floor(z) < r-n+1:
        return 1 - comb(ceil(r-z), n)/comb(r, n)

    return 1.0

def Ez(n: int, r: int, funct: callable):
    e = 0
    
    for z in range(1, r - n +2):
        e += z*funct(z, n, r)

    return e


    
#Main:
    
r = 10
n = 5

verY = []
for y in range(r+1):
    if Fy(y, n, r) != 0:
        verY.append(Fy(y, n, r))



## Funcion de distribución de Y
y = np.array(verY)

yn = np.insert(y, 0, 0)

data = np.arange(5,r+3)

fig, ax = plt.subplots()
ax.set_facecolor('white')


ax.hlines(y=yn, xmin=data[:-1], xmax=data[1:],
          color='blue', zorder=1)

ax.scatter(data[1:-1], y, color='blue', s=18, zorder=2)
ax.scatter(data[1:-1], yn[:-1], color='white', s=18, zorder=2,
           edgecolor='blue')
ax.grid(False)
ax.set_xlim(data[0], data[-1])
ax.set_ylim([-0.01, 1.01])

ax.set_xlabel("y")

ax.set_ylabel("Fy(y)")

ax.set_title("Función de distribución de Y")

plt.show()


## Funcion de densidad de Y

verY = []
for y in range(r+2):
    verY.append(fy(y, n, r))

fig, ax = plt.subplots()

x = np.arange(0, 10 + 2)
y = np.array(verY)
ax.scatter(x, y)
ax.set_xlabel("y")

ax.set_ylabel("fy(y)")

ax.set_title("Función de densidad de Y")

plt.show()

## Meustra las esperanzas de ambas v.a.'s

print(f'La esperanza de y es : {Ey(n, r, fy)}')
print(f'La esperanza de z es : {Ez(n, r, fz)}')


## Funcion de distribución de Z
verZ = []
for z in range(1, r-n+2):
    verZ.append(Fz(z, n, r))

y = np.array(verZ)

yn = np.insert(y, 0, 0)

data = np.arange(1,r-n+4)

fig, ax = plt.subplots()
ax.set_facecolor('white')


ax.hlines(y=yn, xmin=data[:-1], xmax=data[1:],
          color='green', zorder=1)

ax.scatter(data[1:-1], y, color='green', s=18, zorder=2)
ax.scatter(data[1:-1], yn[:-1], color='white', s=18, zorder=2,
           edgecolor='green')
ax.grid(False)
ax.set_xlim(data[0], data[-1])
ax.set_ylim([-0.01, 1.01])

ax.set_xlabel("z")

ax.set_ylabel("Fz(z)")

ax.set_title("Función de distribución de Z")

plt.show()

## Funcion de densidad de Z

verZ = []
for z in range(0, r-n+3):
    verZ.append(fz(z, n, r))

x = np.arange(0, r-n+3)
y = np.array(verZ)

fig, ax = plt.subplots()

ax.scatter(x, y)
ax.set_xlabel("z")

ax.set_ylabel("fz(z)")

ax.set_title("Función de densidad de Z")

plt.show()


