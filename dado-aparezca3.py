# /usr/bin/python
# coding utf8


# Simular el lanzamiento de un dado,que muestre el
# resultado de cada intento y finalice cuando aparezca el 
# lado 3

from random import *
c= 0
x = 0
while x != 3:
    x = randint (1,6)
    c = c+1 
print (x)
print ("Cantidad de lanzamientos hasta que salio el 3: "), c 

