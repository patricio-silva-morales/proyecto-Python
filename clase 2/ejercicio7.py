peso = float(input("Ingrese su peso (en kilos): "))
altura = float(input("Ingrese su altura (en metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    resultado = "BAJO PESO"
elif imc <= 24.9:
    resultado = "PESO NORMAL"
elif imc < 29.9:
    resultado = "SOBREPESO"    
else:
    resultado = "OBESIDAD"
    
print(f"IMC: {imc}. Categoría: {resultado}")