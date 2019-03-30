# /usr/bin/python
# coding utf8

#cauchos
c =  int (input("Ingrese cantidad de cauchos: "))

#precio de venta de cauchos
p = float (input("Ingrese precio: "))

if c > 6:
    
    pv = c*p 
    d = pv*0.15
    vt = pv-d

    print "El precio de venta es:", vt
    print "Su descuento es de:", d
else:
    pv = c*p 
    d = pv*0.1
    vt = pv-d
    
    print "El precio de venta es:", vt
    print "Su descuento es de:", d

