def suma(*args):
    return sum(args)

#print(suma(1,2,3,4,5))

def suma_cuadrados(*args):
    sumaVal = 0
    for num in args:
        sumaVal = sumaVal + num**2
    return sumaVal

print(suma_cuadrados(1,2,3))


def numero_person(nombre, *args):
    suma_numeros = 0
    for num in args:
        suma_numeros = suma_numeros + num
    return (f"{nombre}, la suma de tus números es {suma_numeros}")


