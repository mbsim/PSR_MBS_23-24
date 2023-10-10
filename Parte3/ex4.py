#!/usr/bin/env python
# --------------------------------------------------
# A simple python script to ...
# Miguel Bento Simoes.
# PSR
# --------------------------------------------------
#shebang line to inform the OS that the content is in python

#use imports here

from collections import namedtuple
import math

# define functions here ...

def addComplex(x, y):
    realPart = x.real + y.real
    imaginaryPart = x.imag + y.imag
    complexTuple = complex(realPart, imaginaryPart)
    return complexTuple

def multiplyComplex(x,y):
    realPart = (x.real*y.real) - (x.imag*y.imag)
    imaginaryPart = (x.real * y.imag) + (x.imag* y.real)
    complexTuple = complex(realPart, imaginaryPart)
    return complexTuple

def printComplex(x):
    realPart = x.real
    imaginaryPart = x.imag
    print(f"Complex Number: {realPart} + {imaginaryPart}i")



def main():

    ComplexNumber = namedtuple('ComplexNumber', ['real', 'imag'])
    c1 = ComplexNumber(5, 3)
    print(c1)

    c2 = ComplexNumber(-2, 7)
    print(c2)

    c3 = addComplex(c1, c2)
    print(c3)

    c4 = addComplex(c2, c3)
    print(c4)



if __name__ == "__main__":
    main()
