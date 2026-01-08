venta_total = int(input("Ingrese monto de ventas: $"))

if venta_total > 500000: 
    bono = venta_total * 0.1
else: 
    bono = venta_total * 0.06

print("El bono por sus ventas es de: $", bono)