#uso del input 

dato= input("ingrese un dato: ")

lista = ["nombre", "apellido"]

print(dato)

if lista.count(dato) > 0:
    print("el dato existe:", dato)
else:
    print("el dato no existe", dato)    
 
print("---------------calculadora--------------------")

num1= int(input("primer numero: "))
num2= int(input("segundo numero: "))
suma = num1 + num2
print ( suma)
   
print("---------------validando-------------------")

num1= input("primer numero: ")

try:
    num1 = int(num1)
    
except: 
    num1 = str(num1)
    print("Digite Un numero")
    exit()
    
num2= input("segundo numero: ")

try:
    num2= int(num2)
    
except:
    num = str(num2)
    print("Digite Un numero")
    exit()

suma = num1 + num2
print ( suma)  

print("---------------otro metodo-------------------")

num1= input("primer numero: ")

try:
    num1 = int(num1)
    
except: 
    num1 = "prueba"
if num1 == "prueba":    
    print("El valor ingresado no es un Entero")
    exit()
    
num2= input("segundo numero: ")

try:
    num2= int(num2)
    
except:
    num2 = "prueba"
    
if num2== "prueba":    
    print("El valor ingresado no es un Entero")
    exit()

suma = num1 + num2
print (suma) 

print("------- otras operaciones------------")

simbolo = input("ingrese un simbolo de operacion: ")

if simbolo == "+":
    print ("suma: ", num1 + num2)
elif simbolo == "-":
    print ("resta: ", num1 - num2)
elif simbolo == "*":
    print ("multiplicacion: ", num1 * num2)  
elif simbolo == "/":
    print ("division: ", num1 / num2) 
else:
    print("el numero ingresado no es valido") 
    
    