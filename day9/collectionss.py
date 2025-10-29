from collections import defaultdict, namedtuple

# en caso de pedir una key que no existe, devuelve nada
mi_dic = defaultdict(lambda:"nada")

mi_dic["uno"]="verde"
print(mi_dic["dos"])


Persona = namedtuple("Persona",["nombre","altura","peso"])

ariel = Persona("Ariel",1.76,79)
print(ariel.altura)