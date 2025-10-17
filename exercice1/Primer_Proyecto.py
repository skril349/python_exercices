texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[2]
print(fragmento)

fragmento = texto[:6]
print(fragmento)

fragmento = texto[2:15]
print(fragmento)

fragmento = texto[2:15:2]
print(fragmento)

fragmento = texto[::-1]
print(fragmento)

new_text = "Hola que tal chaval,que soy toni"

resultado = new_text.upper()

print(resultado)

resultado_list = new_text.split()
print(resultado_list)

resultado_list = new_text.split("a")
print(resultado_list)

resultado = new_text.find("a")
print(resultado)


resultado = new_text.replace("a"," ")
print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

new_frase =frase.replace("difícil","fácil")
new_frase= new_frase.replace("mala","buena")
print(new_frase)