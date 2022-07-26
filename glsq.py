#!/usr/bin/env python

import numpy
from scipy.optimize import curve_fit


# definicja x i wzorcowej zaleznosci 
x0=(1,2,4,7,3,6,12,14,16,18,20,23,26)
x0=numpy.array(x0)
a0=2.
z0=3.
y0=a0*x0+z0

# y z szumem
y_rand=y0+numpy.random.normal(0,0.1,len(y0))

###  dopasowanie biblioteka  ####
def fit(x,a,b):
    x=numpy.array(x)
    y = a*x+b
    return y

print("=== curve fit ===")
par, cov = curve_fit(fit, x0, y_rand)
print("a,b= "+str(par))
print("err= "+str(numpy.sqrt(cov[0,0]))+" "+str(numpy.sqrt(cov[1,1])))

### dopasowanie algebraiczne ####
def glsq(X,Y):
    #GLSQ 
    # a,I = glsq(X,Y)
    # Y - wektor dopasowania
    # X - macierz wartosci
    # a - wektor wspolczynnikow
    # I - macierz kowariancji
    X=numpy.matrix(X)
    Y=numpy.matrix(Y)  
    b=Y.getT()
    T=X.getT()
    TX=T*X
    I=TX.getI()
    a=I*T*b   
    return a,I

print("=== glsq ===")

x=numpy.column_stack((x0, [1]*len(x0)))
coe,I = glsq(x,y_rand)

diff = y_rand - (coe[0]*x0+coe[1])
diff=numpy.array(diff)
r = (numpy.sum(diff*diff))
s=numpy.sqrt(r/(len(x0)-2))

print("a,b= "+str(numpy.array(coe)[0])+" "+str(numpy.array(coe)[1]))
print("err= "+str(numpy.sqrt(I[0,0])*s)+" "+str(numpy.sqrt(I[1,1])*s))

print(numpy.std(diff))

