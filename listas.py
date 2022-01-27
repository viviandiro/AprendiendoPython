#la lista con corchetes cuadrados

print("----------------lista---------------")

d = 3.1416
listas = []
lista1 = [1, 0.233, "o", d, [1, 2, 4], (1, 2, 5)]

lista2 = ["hola como estan todos", 1,2,1,1]
vocales = ['a', 'e', 'i', 'o', 'u']
print (lista1, vocales, lista2)
print("---------------append---------------")
lista1.append("prueba")
print(lista1)

print("---------------clear---------------")
#lista1.clear()# limpiar la lista
print(lista1)
print("---------------count---------------")
#se usa para saber cuantas veces se repite un valor
print (vocales, lista2.count(1))

print("------------------------------")
a = 0

for i in lista1:
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
listaDeTupla.append("vivi")# agreg un elemento a la tupla
print(listaDeTupla)

print("------------index------------------")
#nos dice la posicion donde se encuentra un valor

print(tupla.index("revisando"))

print("------------acceso a un elemento-------------------")
tupla1 = ('hola', 'todos', 'revisando')
print(tupla1[1])

print("------------uso del len -------------------")
#cuenta cuantos elementos tiene una tupla
tupla3 = ('a', 'b', 'd')


print (len(tupla3))

print("------------Empaquetado y desempaquetado de tuplas-------")
a=125
b="Gatito"
c="Ana"
d=a,b,c
print (len(d))
print (d)

print("------------Diccionarios-------")






