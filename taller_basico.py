
# NIVEL 1
# 1.1 se solicita el nombre y la edad al usuario con input imprimiendo al final la información recopilada

print("hola, ingresa tu nombre: ")
nombre = input()
edad = int(input("ingresa tu edad: "))

print(f"hola {nombre}, tienes {edad} de edad")


# 1.2 Se realiza una suma simple según lo indica el ejercicio

A = 15
B = 19

# print(A+B)

# 1.3 pedir datos al usuario

base = float(input("ingrese la base del triángulo: "))
altura = float(input("ingrese la altura del triángulo: "))

# calcular el área
area= (base * altura) / 2

print(f"el área del triangulo es: {area}")

# 1.4 se escriben las variables y el tipo de dato que queremos solicitandole al usuario que ingrese un dato
# luego se realiza la operación matemática y se hace el print

celsius = float(input("introduce la temperatura: "))
fahrenheit = (celsius * 9/5) +32

print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit: ")

# 1.5 se escriben diferentes variables para mostrar los tipos que hay incluyendo las listas, tuplas y diccionarios
# se imprimen usando type para que nos muestre el tipo

T1 = 23985
T2 = 239.85
T3 = "BMW F 850 GS ADV"
T4 = True
T5 = ["manzana", 12, 3.1416, True]
T6 = ("manzana", 12, 3.1416, True)
T7 = {"Fruta": "manzana", "cantidad": 12, "pi": 3.1416, "es_correcto": True}

print(type(T1))
print(type(T2))
print(type(T3))
print(type(T4))
print(type(T5))
print(type(T6))
print(type(T7))

# 1.6 se realiza el cálculo de la edad futura usando el dato de la edad que se pidió inicialmente en el taller

edad_futura = edad +10

print(f"En 10 años tendrás {edad_futura} años")


