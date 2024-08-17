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
    print("Tipo de variable")


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
