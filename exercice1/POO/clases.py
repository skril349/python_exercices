
#clase
class Pajaro:
    #metodo constructor
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")
    def volar(self,metros):
        print(f"estoy volando {metros} metros")

mi_pajaro = Pajaro("red","tucan")
mi_pajaro2 = Pajaro("black","cotorra")

print(mi_pajaro.color)
print(mi_pajaro2.color)

