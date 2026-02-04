with open("C:\clon\proyecto-Python\clase 20\lectura_segura.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Buenos días")
    
with open("C:\clon\proyecto-Python\clase 20\lectura_segura.txt", "r", encoding="UTF-8") as archivo:
    contenido = archivo.read()
    
print(contenido)

if archivo.closed:
    print("El archivo fue cerrado automáticamente")