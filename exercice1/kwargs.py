def suma(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        total += value
    print(f"La suma de tus dados es {total}")
suma(x=1, y=2, z=3)

def suma2(num1, num2, *args, **kwargs):
    print(f"numeros = {num1}, {num2}")

    print("args:")
    for arg in args:
        print(f"{arg}")
    print("kwargs: ")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

suma2(3,6,3,6,7,8,x=1, y=2, z=3)


def cantidad_atributos(**kwargs):
    total = 0
    for i in kwargs:
        total += 1
    return total

print(cantidad_atributos(x=1, y=2, z=3))


def lista_atributos(**kwargs):
    lista = []
    for key,value in kwargs.items():
        lista.append(key)
    return lista
print(lista_atributos(x=1, y=2, z=3))


def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")