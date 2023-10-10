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


def main():

    class MyClass:
        y = 2
        x = 5
    p1 = MyClass()
    print(p1.x)   
    print(p1.y)  

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p = Person("John", 36)

    print(p)

    print(p.name)
    print(p.age) 


if __name__ == "__main__":
    main()
