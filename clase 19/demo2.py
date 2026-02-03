try:
    print("Recuperando contenido con read()")
    
    archivo = open("c:\clon\prueba.txt", "r", encoding="utf-8")
    
    contenido = archivo.read()
    
    print(contenido)
    
    archivo.close
    
except FileNotFoundError:
    print("No se encontró el archivo")
    
    
try:
    print("Recuperando contenido con readline()")
    
    archivo = open("c:\clon\prueba.txt", "r", encoding="utf-8")
    
    linea = archivo.readline()
    while linea:
        print(linea, end="")
        linea = archivo.readline()
    
    archivo.close
    
except FileNotFoundError:
    print("No se encontró el archivo")
    
    
try:
    print("Recuperando contenido con readlines()")
    
    archivo = open("c:\clon\prueba.txt", "r", encoding="utf-8")
    
    lineas = archivo.readlines()
    
    for linea in lineas:
        print(linea, end="") 
    
    archivo.close
    
except FileNotFoundError:
    print("No se encontró el archivo")