#!/usr/bin/env python
# -*- coding: utf-8 -*-
print """   A continuación se muestran ejemplos de : 
    (1) Lingüística escrita 
    (2) Lingüística oral 
    (3) No lingüística visual 
    (4) No lingüística gestual
    (5) No lingüística acústica:"""

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
