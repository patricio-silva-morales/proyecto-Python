# Diccionario de producto
# La clave ESPECIFICACIONES tiene otro diccionario como valor
producto = {
    "nombre": "Laptop",
    "precio": 1200,
    "especificaciones": { "RAM": "16GB", "Disco Duro": "512GB SSD" }
}

# Recorro las 3 claves del diccionario producto
for clave, valor in producto.items():
    print(f"{clave} | {valor}")
    
# Recorro el valor (diccionario) de la clave ESPECIFICACIONES
for clave, valor in producto["especificaciones"].items():
    print(f"{clave} | {valor}")