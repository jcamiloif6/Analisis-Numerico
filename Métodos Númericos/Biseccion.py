import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("")
x = symbols('x')
fn = sympify(input("Ingrese la función: "))
f = lambdify(x, fn)

a = float(input("Defina el valor inicial: "))
b = float(input("Defina el valor final: "))
crit = float(input("Defina criterio de tolerancia: "))
i = 0
ea = 1
x_anterior = 0

if f(a) * f(b) < 0:
    print("")
    print("{:^60}".format("Método de Bisección"))
    print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i", "a", "b", "xr", "ea"))
          
    while ea > crit:
        xr = (a + b)/2
        ea = abs(xr - x_anterior)
        
        if f(xr) * f(a) < 0:
            b = xr
        else:
            a = xr
            
        x_anterior = xr
        
        print("{:^10} {:^10} {:^10} {:^10} {:^10}".format(i, a, b, xr, ea))
        i = i +1 
    
    print(" ")
    print("El valor de x es ", round(xr, 9), " con un error de ", ea)

else:
    print(" ")
    print("La función no tiene una raíz en el intervalo de " + "x = " + str(a) + " a x = " + str(b))
    print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i", "a", "b", "xr", "ea"))
          

     
            

