# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math

complex1 = input()
complex1 = complex(complex1)
x = complex1.real
y = complex1.imag
r = x**2 + y**2
print(math.sqrt(r))
print(cmath.phase(complex(x,y)))
