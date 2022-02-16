print("---------------funciones -----------")
def miFuncion():
    print(" hola ")
    
miFuncion()

print("------------------------------------")
def miDato(argumento):
    print("hola", argumento)
    
miDato("como estan")
    
print("------------------------------------")
def miDatos(argumento1, argumento2):
    print("hola", argumento1, argumento2)
    
miDatos("como estan", "todos") 

print("------------------------------------")
def miNombre(*nombre):
    print("hola", nombre[3])
    
miNombre("ccamilo", "jose", "daniel", "pedro")    

print("------------------------------------")
def misDatos(nombre, apellido):
    print("hola", nombre, apellido)
    
misDatos(nombre="jose", apellido= "jaimes")   

print("------------------------------------")
def misDatos2(**args):
    print("hola", args["nombre"], args["apellido"])
    
misDatos2(nombre="Camilo", apellido= "jaimes") 

print("------------------------------------")
def misDatos3(argus =" jhon "):
    print("hola", argus)
    
misDatos3("garcia") 
misDatos3()

print("------------------------------------")
def miNuevaLista(lista):
    for el in lista:
        print(el)
miNuevaLista(["hola", "mundo"])

print("------------------------------------")               
def miConcatenacion(lista):
    i =""
    for el in lista:
        i = i + el + ""
    return i    
        
nombre = miConcatenacion(["hola", "  mundo"])
print(nombre)

print("------------------------------------")
def recursividad(i):
    if ( i < 1):
        return i    
    print(i)    
    recursividad(i - 1)
    
recursividad(6)   
