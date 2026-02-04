try:
    
    archivo = open(r"C:\clon\proyecto-Python\clase 20\archivo_seguro.txt", "r")
    
    print(archivo.read())
    
    archivo.close()

except FileNotFoundError:
    print("El archivo no existe")
    
finally:
    print("Gracias por utilizar la aplicación")