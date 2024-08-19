def listas():
    """

    """
    todo = [
        "pruebas1",
        "pruebas2",
        "pruebas3",
        "pruebas4",
        "pruebas5",
    ]
    print(todo)
    numbers = [1, 2, 3, 4, 5, "seis"]
    print(type(numbers))
    mix = ["uno", 2, 3.14, True, [1,2,3]]
    print(mix)

def operaciones_matematicas():
    a = 10
    b = 2
    print(f"Los valores de a y b son {a} y {b}")
    print(f"suma = {a + b}")
    print(f"resta = {a - b}")
    print(f"multiplicacion = {a * b}")
    print(f"division = {a / b}")
    print(f"division entera = {a // b}")
    print(f"modulo = {a % b}")
    print(f"exponente = {a ** b}")

    operacion_1 = 2 + 3 * 4
    operacion_2 = (2 + 3) * 4
    operacion_3 = 2 + (3 * 4)
    print(f"operacion_1 = {operacion_1}, operacion_2 = {operacion_2}, operacion_3 = {operacion_3}")


def enteros_flot_bool():
    x = 10
    y = 5.578
    z = 1.2e6
    print(f"X es de tipo: {type(x)}")
    print(f"Y es de tipo: {type(y)}")
    print(f"Z es de tipo: {type(z)} y el valor es: {z}")
    print(f"""
        La suma de los valores x + y = {z + y}
    """)

    is_true = True  # Valor booleano
    is_false = False
    print(f"Los boobleanos son True: {is_true} y False: {is_false}")


def metodos_variables():
    texto = "hola mundo, hola"
    print("count: ", texto.count("hola"))  # Salida: 2

    texto = "hola mundo"
    print("capitalize: ", texto.capitalize())  # Salida: "Hola mundo"

    texto = "hola mundo"
    print("title: ", texto.title())  # Salida: "Hola Mundo"

    texto = "Hola Mundo"
    print("swapcase: ", texto.swapcase())  # Salida: "hOLA mUNDO"

    texto = "hola mundo"
    print("replace: ", texto.replace("hola", "adios"))  # Salida: "adios mundo"

    texto = "hola mundo"
    print("split: ", texto.split())  # Salida: ["hola", "mundo"]

    texto = "  hola mundo  "
    print("strip: ", texto.strip())  # Salida: "hola mundo"

    texto = "  hola mundo"
    print("lstrip: ", texto.lstrip())  # Salida: "hola mundo"

    texto = "hola mundo  "
    print("rstrip: ", texto.rstrip())  # Salida: "hola mundo"

    texto = "hola mundo"
    print("find: ", texto.find("mundo"))  # Salida: 5

    texto = "hola mundo"
    print("index: ", texto.index("mundo"))  # Salida: 5

    expresion = "3 + 5"
    print("eval: ", eval(expresion))  # Salida: 8

    expresion = "HOLA MUNDO"
    print("Lower: ", expresion.lower())  # Salida: hola mundo

    expresion = "hola mundo"
    print("Lower: ", expresion.upper())  # Salida: HOLA MUNDO

    codigo = """for i in range(5):    print(i)"""
    exec(codigo)
    # Salida:
    # 0
    # 1
    # 2
    # 3
    # 4

    print("esta", "es", "una", "practica", sep=", 😁 ")
    print("esta", end=" ")
    print("es una practica")


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
            1: Tipo de variable
            2: Metodos de variable
            3: Enteros, Flotantes y Booleanos
            4: Operaciones matematicas
            5: Listas
            """
    tipo_teoria = input(f"Que tipo de teoria quiere ver? \n {teoria}\n >> ")
    if tipo_teoria == "1":
        tipo_variables()
    if tipo_teoria == "2":
        metodos_variables()
    if tipo_teoria == "3":
        enteros_flot_bool()
    if tipo_teoria == "4":
        operaciones_matematicas()
    if tipo_teoria == "5":
        listas()
