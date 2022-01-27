#la lista con corchetes cuadrados

print("----------------lista---------------")

d = 3.1416
listas = []
lista1 = [1, 0.233, "o", d, [1, 2, 4], (1, 2, 5)]

lista2 = ("hola como estan todos")
vocales = ['a', 'e', 'i', 'o', 'u']
print (lista1, vocales, lista2)

a = 0

for i in lista2:
    if i in vocales:
        a += 1

print(a)

#reverse
print("----------------------Reverse------------")

lista1.reverse() #muestra la lista invertida
print(lista1)
#----------------
print("----------------------sort------------")
prueba1 = ["hola","camila", "avion", "vocales"]
# se utiliza para ordenar listas y deben ser del mismo tipo numeros o palabras
prueba1.sort()
numeros = [16, 4, 9, 1, 3, 20, 8]
numeros.sort()
print(numeros)
print(prueba1)

# definicion de tupla son parentisis
#son objetos de tipo secuencia y no se puede modificar 
# ejemplo
print("----------------tupla---------------")

tupla= ('hola', 'todos', "revisando")
listaDeTupla=list(tupla)
listaDeTupla.append("vivi")
print(listaDeTupla)
print("-------------------------------")
tupla1 = ('hola', 'todos', "revisando")
tupla1[1]
print(tupla)









