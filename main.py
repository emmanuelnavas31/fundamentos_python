from app.practica.Practica import main_practica
from app.teoria.Teoria import main_teoria


if __name__ == '__main__':
    def f(x):
        return x * 2


    print("valor = ", f(3))

    opciones = """
    '1': "Teoria"
    '2': "Practica"
    """

    option = int(input(f"Escribe un numero de las siguientes opciones \n {opciones} > "))
    if option == 1:
        main_teoria()
    elif option == 2:
        main_practica()
