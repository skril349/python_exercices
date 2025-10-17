nombres = ["Juan","Ana","Joan","Belen"]
for nombre in nombres:
    print(f"hola {nombre}")

numero = 10

while numero != -1:
    print(numero)
    numero = numero - 1

mi_lista = []
for i in range(3,300):
    if(i % 3 == 0):
        mi_lista.append(i)
print(mi_lista)

lista = ["a","b","c","d","e","f"]

for indice,item in enumerate(lista):
    print(indice,item)
