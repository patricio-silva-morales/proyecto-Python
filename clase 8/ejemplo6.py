estudiantes = [("Ana Pérez", 22, "Santiago"),("Carlos Muñoz", 25, "Santiago"),("María González", 20, "Concepcion"),("Javier Rojas", 23, "La Serena"),("Fernanda Soto", 21, "Temuco")]

#Recorre lista y muestra estudiantes
for estudiante in estudiantes:
    print (f"El estudiante {(estudiante[0])}, edad: {(estudiante[1])} de la ciudad: {(estudiante[2])}")

agregar_nombre = input("Ingrese el nombre del estudiante:..")
agregar_edad = int(input("Agregue la edad:..."))
agregar_ciudad = input("Ingrese la ciudad:...")

contar_ciudad = input("Ingrese la ciudad que quiere consultar:...")

# Tupla 
nuevos_datos = (agregar_nombre, agregar_edad, agregar_ciudad)

#Agrega nuevos datos a la lista
estudiantes.append(nuevos_datos)

#Recorre lista y suma ciudades repetidas
contador = 0
for estudiante in estudiantes:
    if contar_ciudad == estudiante[2]:
        contador += 1        

#Recorre lista y suma edad, mas un contador de veces recorrido
contador2 = 0
contador3 = 0
for estudiante in estudiantes:
    contador2 += estudiante[1]
    contador3 += 1

print (f"El promedio de las edades de los estudiantes es: {int(contador2/contador3)}")    
    
print (f"Existen {contador} estudiantes que pertenecen a esa ciudad.")


print (estudiantes)