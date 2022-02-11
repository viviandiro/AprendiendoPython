x = 0
while x < 5: 
    print(x)
    if x == 3: # con el break el codigo se detiene en 3 segun la condicion
        break
    x += 1
    
#uso del continue    
print("------------continue----")  
 
x = 0
while x < 5: 
    x += 1
    if x == 3: #con el continue el codigo continua y omite el 3 hasta llegar a 5 en este caso
        continue
    print(x)

print("---------pass-------")

x = 0
while x < 5: 
    x += 1
    if x == 3: #con el pass omite el condicional y continua hasta completar el bucle
        pass
    print(x)
    
print("---------for -------")   

usuarios = ["carlos","manuel","jhon","jairo","andres"]

for usuario in usuarios:
    print(usuario)
    
print("----------------")    
user = "jhon jairo"

for o in user:
    print(o)

print("----------------") 
    
usuarios = ["carlos","manuel","jhon","jairo","andres"]

for usuario in usuarios:
    if usuario == "jhon":
        break
    print(usuario)
    
print("-----for-----------") 


usuarios = ["carlos","manuel","jhon","jairo","andres"]

for usuario in usuarios:
    if usuario == "jhon":
        continue
    print(usuario)
    
print("-------range---------")  

for x in range(3, 50, 5):
    print(x)  
else:
    print("Hemos terminado exitosamente!!!!")
    
print("-------for dentro de for---------")

usuarios = ["carlos","manuel","jhon","jairo","andres"]

edades=["15","20","25","28","23"]

for usuario in usuarios:
    for edad in edades:
        print (usuario,edad + " todas las edades")


