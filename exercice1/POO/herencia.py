class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("este animal ha nacido")

    def hablar(self ):
        print("Este animal emite un sonido")


class Pajaro(Animal):

    def __init__(self,edad,color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self,metros):
        print(f"estoy volando {metros} metros")

piolin = Pajaro(2,"red",60)
mi_animal = Animal(5,"negro")

piolin.nacer()
piolin.hablar()
piolin.volar(100)

mi_animal.nacer()
mi_animal.hablar()
