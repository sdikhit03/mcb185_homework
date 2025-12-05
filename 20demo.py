# 20demo.py by Saumitra Dikhit
import math
import random
'''

t = 1,2
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

#print(midpoint(1, 2, 3, 4))
#m = midpoint(1, 2, 3, 4)
#mx, my = midpoint(1, 2, 3, 4)
#print(mx, my)
#print(m[0], m[1])

i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

for i in range (1, 10, 3): print(i)

for i in range(0, 5): print(i)

for i in range(5): print(i)

for i in range(4, -1, -1): print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)

for i in range(len(basket)):
    print(basket[i])


for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else: print(i, 'is odd')

for i in range(5):
    print(random.random())

for i in range(3):
    print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(3)
print(random.random())
print(random.random())



# practice problems
def triangle(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + i
    return sum
# print(triangle(6))

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
# print(factorial(3))

def poisson(n, k):
    return n**k * math.e**-n / factorial(k)
# print(poisson(2, 4))

def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
# print(nchoosek(4, 2))

def euler(lim):
    num = 0
    for i in range(lim):
        num = num + 1/factorial(i)
    return num
# print(euler(100))

def isprime(num):
    if num <= 1: return False
    for div in range(2, num//2 + 1):
        if num % div == 0: return False
    return True
# print(isprime(1))

def nilakantha(lim):
    num = 3
    for i in range(1, lim + 1):
        x = i * 2
        prod = x * (x + 1) * (x + 2)
        if i % 2 == 1: num = num + 4/prod
        else: num = num - 4/prod
    return num
# print(nilakantha(1000))

def montecarlo():
    inside = 0
    outside = 0
    while True:
        x = random.random()
        y = random.random()
        dist = math.sqrt(x**2 + y**2)
        if dist < 1: inside += 1
        else: outside += 1
        print((inside / (inside + outside)) * 4)
montecarlo()
'''
def ddstats():
    # 3D6
    tot = 0
    for i in range(3):
        sum = 0
        for i in range(3):
            sum += random.randint(1, 6)
        tot += sum
    avg = tot/3
    print('Avg Stat Value (3D6):', avg)

    # 3D6r1
    tot = 0
    for i in range(3):
        sum = 0
        idx = 0
        while(idx < 3):
            num = random.randint(1, 6)
            print (num)
            if(num != 1):
                sum += num
                idx += 1
        tot += sum
    avg = tot/3
    print('Avg Stat Value (3D6r1):', avg)

    # 3D6x2
    tot = 0
    for i in range(3):
        sum1, sum2, sum3 = 0
        
    avg = tot/3
    print('Avg Stat Value (3D6x2):', avg)


ddstats()