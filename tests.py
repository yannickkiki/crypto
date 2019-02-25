#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:58:27 2019

@author: yannick
"""

import sympy
import math

n=262158157939114458143411
prime_number=sympy.prevprime(1+int(math.sqrt(n)))
while True:
    operand,r=divmod(n,prime_number)
    print(operand,r)
    if r==0 and sympy.isprime(operand):
        print(f"p={prime_number}, q={operand}")
        break
    else:
        prime_number=sympy.prevprime(prime_number)
        print(prime_number)
#Résultat: p=512011737421, q=512015914439
        
n=262158157939114458143411
prime_number=sympy.prevprime(1+int(math.sqrt(n)))
while True:
    operand=n/prime_number
    if int(operand)==operand and sympy.isprime(int(operand)):
        print(f"p={prime_number}, q={int(operand)}")
        break
    else:
        prime_number=sympy.prevprime(prime_number)
#Résultat: p=512011737421, q=512015914439, not sure
        
sympy.ntheory.factorint(25) 

print("1")