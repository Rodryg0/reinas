import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol
from scipy.misc import derivative 
x=Symbol('x')
y=x**4/4-9*x**2/2
d=y.diff(x)
sd=d.diff(x)
print("Funcion original: ",y)
print("Primera Derivada: ",d)
print("Segunda Derivada: ",sd)

x0=0
x1=-3
x2=3

s = "x**4/4-9*x**2/2"

eval1 = {"x": x0}
punto1=eval(s, {}, eval1)
print("Punto 1: (",x0,",",punto1,")")

eval2 = {"x": x1}
punto2=eval(s, {}, eval2)
print("Punto 2: (",x1,punto2,")")

eval3 = {"x": x2}
punto3=eval(s, {}, eval3)
print("Punto 3: (",x2,",",punto3,")")


def f(x):
    return x**4/4 - 9*x**2/2
 
N=500;
a=-10
b=10
x=np.linspace(a,b,N)

y=f(x)
plt.plot(x,y,'g-')
plt.show
