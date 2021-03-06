import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol
from scipy.misc import derivative 
x=Symbol('x')
y=x**4
d=y.diff(x)
sd=d.diff(x)
print("Funcion original: ",y)
print("Primera Derivada: ",d)
print("Segunda Derivada: ",sd)
f=lambda x:sd
print("Funcion Evaluada",derivative(f,0,dx=1e-6))

def f(x):
    return x**4 


N=150;
a=-50
b=50
x=np.linspace(a,b,N)
dx=(b-1)/(N-1)

y=f(x)
plt.plot(x,y,'g-')
plt.show
