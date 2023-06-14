comidas = []

def show_comidas():
    for comida in comidas:
        print(f"comidas { comida }")

def add_comida(comida):
    comidas.append(comida)

def del_comida(comida):
    try:
        comidas.remove(comida)
    except Exception:
        print("no se encontro en la lista")

text_menu = '''
elige una opcion:
    1- agregar comida
    2- eliminar comida
    3- mostrar comidas
    4- salir
'''

while True:
        choice_user =int(input(text_menu))
        if choice_user == 1:
            comida = input("escribe una comida: ")
            add_comida(comida)
        elif choice_user == 2:
            comida =input("escribe una comida: ")
            del_comida(comida)
        elif choice_user == 3:
            show_comidas()
        elif choice_user == 4:
            break
        else:
            print("escribe bien :/")
            
