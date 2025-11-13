# # entrada = ""

# # while entrada != "x":
# #     print("sigue adentro")
# #     entrada = input("ingrese x para salir: ")

# curso_python = {
#     "nombre_curso": "Introducción a Python",
#     "duracion_horas": 20,
#     "estudiantes": ["Ana", "Luis", "Sofía"],
#     "activo": True
# }

# print(list(curso_python.keys()))
# print(list(curso_python.values()))

# for clave, valor in curso_python.items():
#     print(f"{clave}: {valor}")

# nivel = curso_python.get("nivel", "principiante")
# print("Nivel del curso:", nivel)

coders = []
print(coders)

amaount = int(input("Cuantos coders va a ingresar: "))

while amaount != 0 : 

    name =  input("Ingrese su nombre: ")
    lastname =  input("Ingrese su apellido: ")
    age =  input("Ingrese su edad: ")
    email =  input("Ingrese su email: ")

    coder = {
        "Nombre": name,
        "Apellido": lastname,
        "Edad": age,
        "Email": email
    }
    coders.append(coder)
    amaount -= 1
print(coders)