dic = {"Clave1":100, "Clave2":200, "Clave3":300}

dic.popitem()

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

texto.lstrip("':%_#")
print(texto)

def todos_positivos(lista):
    for i in lista:
        if i < 0 :
            return False
        else:
            pass
    return True

lista = [1,2,3,67,3,5,7]
print(todos_positivos(lista))