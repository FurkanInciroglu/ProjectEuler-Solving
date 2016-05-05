#!/usr/bin/env python
# -*- coding: utf-8 -*-



def Polindrome(a):
         word = str(a)
         if word == ''.join(reversed(word)):
             return True

for x in range(900, 1000):
    for y in range(900, 1000):
        multiple = x*y
        if Polindrome(multiple):
            print multiple

