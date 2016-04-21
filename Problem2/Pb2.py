#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Fibo(n):

    if n == 1 or n == 2:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)


i = 1
sum = 0

while Fibo(i) < 4000000:
    if Fibo(i) % 2 == 0:
        sum += Fibo(i)
    i += 1
print (sum)
