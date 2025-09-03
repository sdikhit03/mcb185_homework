# 10demo.py by Saumitra Dikhit

import math

print("hello, again") # greeting

print(1.5e-2)
print(5 // 2)
print(5 % 2)
print(round(3.14159, ndigits = 3))
print(math.ceil(3.14))
print(math.sqrt(49))
print(math.factorial(3))
print(0.1 * 3)

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

hyp = pythagoras(3,4)
print(hyp)

# functions practice

def area_circle(r): return math.pi * r**2
def area_rectangle(l, w): return l * w
def f_to_c(f): return (f-32) / 1.8
def harmonic_mean(a, b, c): return 3 / (1/a + 1/b + 1/c)

print(f_to_c(100))
print(harmonic_mean(1,2,3))

# conditionals
a = 2
b = 2
if a == b:
    print('a equals b')
print(a, b)

def is_even(x):
    if x % 2 == 0: return True
    return False

print(is_even(2))
print(is_even(3))

# NEVER test for equality with floating point numbers
a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print ('a > b')
else: print ('a == b')

def silly(m, x, b):
    y = m * x + b

print(silly(2, 3, 4))


# More Practice
def is_integer(num): return num % 1 == 0
print(is_integer(2))
print(is_integer(2.5))

def is_probability(num):
    if (0 <= num) and (num <= 1):
        return True
    return False
print(is_probability(0.6))
print(is_probability(1.2))

def mol_weight(nuc):
    if (nuc == "a" or nuc == "A"): return "331.2 g/mol"
    elif (nuc == "c" or nuc == "C"): return "307.2 g/mol"
    elif (nuc == "t" or nuc == "T"): return "322.2 g/mol"
    elif (nuc == "g" or nuc == "G"): return "347.2 g/mol"
print(mol_weight("a"))
print(mol_weight("u"))

def complement_nuc(nuc):
    if (nuc == "a" or nuc == "A"): return "T"
    elif (nuc == "c" or nuc == "C"): return "G"
    elif (nuc == "t" or nuc == "T"): return "A"
    elif (nuc == "g" or nuc == "G"): return "C"
print(complement_nuc("T"))
print(complement_nuc("U"))