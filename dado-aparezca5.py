# /usr/bin/python
# coding utf8


# Simular el lanzamiento de un dado y determina la cantidad de lanzamientos
#hasta que salga el numero 5

from random import *

x = 0
i = 0
while True:
      x = randint (1, 6)
      print(x)
      i = i + 1
      if x == 5:
            break
      print("El lanzamiento en el que salio el 5 fue:") , i 