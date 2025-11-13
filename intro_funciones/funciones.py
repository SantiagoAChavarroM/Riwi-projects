# def sum_numeros(*numeros):
#     print(numeros)
#     resultado = sum(numeros)
#     print(resultado)

# sum_numeros(1,2,3,4,5,6,7)

# # *args argumentos posicionales arbitrarios, empaqueta en tupla

# # **kwargs argumentos arbitrarios

# def imprimir_info(**info):
#     for clave, valor in info.items():
#         print(f"{clave}: {valor}")



# imprimir_info(nombre="Juan", edad=25, ciudad="ejemplo")

# def función_combinada(*args, **kwargs):
#     print("argumentos posicionales", args)
#     print("argumentos de palabra clave:", kwargs)


# función_combinada(1, 2, 3, nombre="juan", edad=25)

# def suma(a, b, c):
#     resultado = a + b + c
#     return resultado

# resultado_suma = suma(5, 5, 1)
# print(resultado_suma)

# def función_condicional(a, b):
#     suma = a + b
#     resta = a - b
#     división = a / b
#     multiplicación = a * b
#     return suma, resta, multiplicación, división

# resultado = función_condicional(8, 4)
# print(resultado)

# ambitos variables (local y global)

# def funcion():
#     x = 10
#     print(x)

# funcion()

# x = 10

# def funcion():
#     global x
#     x = 20
#     print(x, "print inside")

# funcion()
# print(x, "print outside")

