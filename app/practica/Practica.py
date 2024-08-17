def metodos_variables():
    print("""
    .count() 
    .capitalize()
    .title() 
    .swapcase() 
    .replace(,) 
    .split() 
    .strip() 
    .lstrip() 
    .rstrip() 
    .find()
    .index() 
    eval()	#Este y el siguiente son super métodos
    exec()
    """)


def tipo_variables():
    name = str(input("Ingrese el nombre: "))
    edad = int(input("Ingrese la edad: "))
    direccion = str(input("Ingrese la direccion: "))
    estatura = int(input("Ingrese la estatura: "))
    peso = int(input("Ingrese el peso: "))

    print(f"El nombre ingresado es {name} y es de tipo {type(name)}\n"
          f"la edad es {edad} y es de tipo {type(edad)}\n"
          f"la dirección es {direccion} y es de tipo {type(direccion)}\n"
          f"la estatura es {estatura} y es de tipo {type(estatura)}\n"
          f"el peso es {peso} y es de tipo {type(peso)}\n"
          )



def main_practica():
    teoria = """
            '1': "Tipo de variable"
            '2': "Metodos de variable"
            """
    tipo_teoria = input(f"Que tipo de teoria quiere ver? \n {teoria}\n >> ")
    if tipo_teoria == "1":
        tipo_variables()
    if tipo_teoria == "2":
        metodos_variables()
