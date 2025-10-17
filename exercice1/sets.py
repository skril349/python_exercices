texto = input("introduce un texto: ")
letras = input("introduce tres letras: ")

#1 quants cops apareix la lletra
texto = texto.lower()
letras = letras.lower()
for letra in letras:
    print(f"la letra {letra} apareix {texto.count(letra)}")
#2quantes paraules hi ha al text
print("separació de les paraules en array:\n")
print(texto.split())

#3 primera i ultima lletra del text
print(f"primera lletra del text es {texto[0]}, ultima lletra es {texto[-1]}")
#4 invertir el text
print(texto[::-1])
#5 apareix la paraula python al text?
if texto.find("Python"):
    print(True)
else:
    print(False)
