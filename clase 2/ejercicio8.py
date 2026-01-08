nota = float(input("Ingrese nota de la evaluación: "))

if nota < 4.0:
    categoria = "Reprobado"
elif nota <= 5.4:
    categoria = "Suficiente"
elif nota <= 6.4:
    categoria = "Bueno"
elif nota <= 6.9:
    categoria = "Muy bueno"
else:
    categoria = "Excelente"

print(f"Nota: {nota} Clasificación: {categoria}")