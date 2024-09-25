#Para crear una variable solo se necesita el nombre y el valor
#hay diferentes tipo de variables. Sus nombres deben empezar en minusculas
#si son dos palabras se utiliza camelCase(ejemplo: nombreVariable)

nombre = "Carlos" #string
edad = 23 #int
sexo = 'M' #char
vivo = True #bool
altura = 1.75 #float

nombre2= input("introduzca su nombre: ")
print(nombre2)

#Castear
edad2 = int(input("introduzca su edad: "))
print(edad2)

print("Variable nombre2: ", type(nombre2))
print("Variable edad2: ",type(edad2))