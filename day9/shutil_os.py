import os 
import shutil
import send2trash

print(os.getcwd())

# archivo = open("curso.txt","w")
# archivo.write("texto de prubea")
# archivo.close()

#mover archivos
#shutil.move("curso.txt", "C:\\Users\\antoni\\Documents\\Udemy\\python_exercices")
ruta = "C:\\Users\\antoni\\Documents\\Udemy"

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f"En la carpeta: {ruta}")
    print(f"Las subcarpetas son")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")