
# print archivo read
mi_archivo = open("prueba.txt","r")
print(mi_archivo.read())
# sempre tancar fitxer al obrirlo
mi_archivo.close()


mi_archivo = open("prueba.txt","w")
mi_archivo.write(" soy el nuevo texto")
# sempre tancar fitxer al obrirlo
mi_archivo.close()