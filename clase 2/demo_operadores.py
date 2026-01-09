nota1 = float(input("Ingrese la nota 1 (1.0-7.0): "))
nota2 = float(input("Ingrese la nota 2 (1.0-7.0): "))
nota3 = float(input("Ingrese la nota 3 (1.0-7.0): "))

promedio_final = (nota1 + nota2 + nota3) / 3

print("Promedio final: ", promedio_final)

porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia (0-100): "))

if (promedio_final >= 4.0) and (porcentaje_asistencia >= 70):
    print("Aprobado")
else:
    print("Reprobado")