with open("C:\clon\proyecto-Python\clase 20\demo_escritura.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Esta es la primera línea\n")
    archivo.write("Esta es la segundo línea\n")
    
    lineas = [
        "Esta es la tercera línea\n",
        "Esta es la cuarta línea\n",
        "Esta es la quinta línea\n"
    ]

    archivo.writelines(lineas)
    
print("Gracias por utilizar la aplicación")