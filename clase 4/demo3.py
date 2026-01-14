temperatura = float(input("Ingrese una temperatura: "))

if temperatura < 10:
    print("Abrigo grueso y bufanda")
elif temperatura <= 20:
    print("Chaqueta ligera")
elif temperatura <= 30:
    print("Ropa cómoda y fresca")
else:
    print("Ropa ligera y protector solar")