#!/usr/bin/env python
# -*- coding: utf-8 -*-
print """   A continuaci�n se muestran ejemplos de : 
    (1) Ling��stica escrita 
    (2) Ling��stica oral 
    (3) No ling��stica visual 
    (4) No ling��stica gestual
    (5) No ling��stica ac�stica:"""

l = []

print " La correspondencia por carta"
m = raw_input("")
m = int(m)
l = l + [m]
print " Cuando conversamos"
m = raw_input("")
m = int(m)
l = l + [m]
print " La publicidad "
m = raw_input("")
m = int(m)
l = l + [m]
print " Los gestos que utilizamos a diario"
m = raw_input("")
m = int(m)
l = l + [m]
print " La sirena de la ambulancia "
m = raw_input("")
m = int(m)
l = l + [m]

n = 0
k = 1
for m in l:
    if l[m -1] == k:
        n = n + 1
    k = k + 1 

print "Obtuviste "
print n 
print " correcta/s"
