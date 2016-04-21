#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

def PrimeFactors(n):

    Factor = []
    a = 2

    while n > 1:
        while n%a==0:
            n = n/a
            Factor.append(a)
        a +=1
    return Factor

print PrimeFactors(100)