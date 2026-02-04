import os
import shutil

with open("C:\clon\proyecto-Python\clase 20\demo_archivo.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Bootcamp\n")
    archivo.write("Lección: Manejo de Archivos\n")

# Renombrar el archivo
os.rename(r"C:\clon\proyecto-Python\clase 20\demo_archivo.txt", r"C:\clon\proyecto-Python\clase 20\archivo_renombrado.txt")

# Mover el archivo
shutil.move(r"C:\clon\proyecto-Python\clase 20\archivo_renombrado.txt", r"C:\clon\proyecto-Python\clase 20\nueva_carpeta")