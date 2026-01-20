from collections import defaultdict

# Ejemplo con defaultdict
# En este caso el tipo por defecto es int
contadores = defaultdict(int)

contadores["python"] += 1

print(contadores["python"])


