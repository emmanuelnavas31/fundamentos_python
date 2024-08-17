def semantica():
    print("""
        SEMANTICA\n

        Es el sentido que nosotros  vamos a darle al codigo. es decir si tenemos una entrada de numeros tendriamos
        que devolver numeros para que exista la consistencia de los datos. 
        """)


def sintaxis():
    print("""
        SINTAXIS

        se refiere a la manera que nosotros vamos a escribir codigo y siguiendo las buenas practicas
    """)


def variables():
    print(
        """
        Una variable en Python es un nombre que se utiliza para almacenar datos que pueden ser usados y manipulados a lo largo del programa. Piensa en una variable como un contenedor o una etiqueta que apunta a un valor específico, como un número, una cadena de texto, una lista, entre otros.

        Cómo declarar una variable en Python
        Declarar una variable en Python es muy sencillo. Solo necesitas escribir el nombre de la variable, seguido de un signo igual =, y luego el valor que quieres asignarle. No es necesario especificar el tipo de dato de la variable, ya que Python lo infiere automáticamente según el valor asignado.
        
        Ejemplos de declaración de variables:
        Variable numérica (entero):
        
        edad = 25
        Aquí, edad es una variable que almacena el valor entero 25.
        
        Variable de texto (cadena):
        
        nombre = "Juan"
        En este caso, nombre es una variable que almacena la cadena de texto "Juan".
        
        Variable de punto flotante (decimal):
        
        temperatura = 36.6
        Aquí, temperatura es una variable que almacena el valor decimal 36.6.
        
        Variable booleana (verdadero o falso):
        
        es_mayor_de_edad = True
        es_mayor_de_edad es una variable que almacena el valor booleano True (verdadero).
        
        Variable de lista:
        
        numeros = [1, 2, 3, 4, 5]
        En este ejemplo, numeros es una variable que almacena una lista de números.
        
        Convenciones para nombrar variables en Python:
        Nombres descriptivos: Es recomendable usar nombres de variables que describan claramente su propósito. Por ejemplo, en lugar de x, usar edad si la variable almacena una edad.
        No usar palabras reservadas: No puedes usar palabras reservadas del lenguaje (como if, for, while, etc.) como nombres de variables.
        Usar guiones bajos para separar palabras: Si el nombre de la variable consta de varias palabras, usa guiones bajos para separarlas, como numero_de_estudiantes.
        Sensible a mayúsculas y minúsculas: Python diferencia entre mayúsculas y minúsculas, por lo que edad y Edad serían dos variables distintas.
        Ejemplo completo:

        nombre = "Ana"              # Variable de cadena
        edad = 30                   # Variable entera

        es_estudiante = False       # Variable booleana
        altura = 1.65               # Variable de punto flotante
        materias = ["Matemáticas", "Física", "Química"]  # Variable de lista
        
        print(f"{nombre} tiene {edad} años, mide {altura} metros y está estudiando {materias[0]}.")
        En este ejemplo, hemos declarado varias variables de diferentes tipos y las hemos utilizado en una declaración print para mostrar un mensaje.
        """
    )


def main_teoria():
    teoria = """
        '1': "Que es la semantica"
        '2': "Sintaxis en python"
        '3': "Declaración de variables"
        """
    tipo_teoria = input(f"Que tipo de teoria quiere ver? \n{teoria} >> ")
    if tipo_teoria == "1":
        semantica()
    if tipo_teoria == "2":
        sintaxis()
    if tipo_teoria == "3":
        variables()
