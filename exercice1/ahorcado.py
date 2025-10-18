vidas = 6
resuelto = 1



def crear_palabra(word_to_find):
    clave_valor = {}
    for index,letter in enumerate(word_to_find):
        clave_valor[index] = letter.capitalize()
    longitud = len(word_to_find)
    guiones = "_" * longitud
    return clave_valor, list(guiones)

def crear_guiones(letter_to_find, clave, guiones):
    indices = [k for k, v in clave.items() if v == letter_to_find]
    for index in indices:
        guiones[index] = letter_to_find
    return guiones





    return 0

word_to_find = input("Ingrese una palabra: ")
clave, guiones = crear_palabra(word_to_find)
print(f"vidas = {vidas} ")
print(guiones)


while resuelto == 1:
    letra_a_buscar = input("Ingrese una letra: ")

    if letra_a_buscar.capitalize() in clave.values():
        print(f"vidas = {vidas} ")
        guiones = crear_guiones(letra_a_buscar.capitalize(), clave, guiones)
        print(guiones)

        if guiones.count("_") == 0:
            print("you win !")
            break


    else:
        vidas -= 1
        print(f"vidas = {vidas} ")
        print(guiones)
        if vidas == 0:
            break

# info a nova branca
