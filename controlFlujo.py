#usi del if
print("-------if-----------------------")

if 3 < 5:
    print(" 3 es menor q 5")
if 3 == 5:
    print(" 3 es igual q 5")
if 3 > 5:
    print(" 3 es mayor q 5")
if 3 != 5:
    print(" 3 es diferente q 5")
    
print("-------if-- else-- elif-----------------------")   

if 3 > 5:
    print(" error")
elif 3 == 5:
    print("3 es igualq 5")
elif 5 != 5:
    print("3 es diferente 5")    
else:
    print(" ninguna de las anteriores es verdadera")

print("-----------------------------")
if 3 > 5:
    print("3 es mayor que 2")

else:
    print("si la anterior es false me imprimo")
    
print("-------if cortos y ternarios----------------------")   

if 3 < 5: print("Mis numeros estan CORRECTOS")

print("devuelve true")if 3==4 else print("devuelve false")

print("------and y or----------------")
#ambas condiciones deben ser verdaderas si alguna es falsa no se imprime
if 8 > 5 and  5 > 4:
    print("ambas son correctas")
#si una condiciones son verdaderas se ejecutan la instruccion o ambas tambien puede ser true
if 7 < 5 or 2 < 5:
    print("una es correcta ")
# si ambas son falsas no se ejecutan  
if 7 < 5 or 2 > 5:
    print("falsas")
 