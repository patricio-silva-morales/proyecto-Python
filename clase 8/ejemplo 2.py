# Lista tareas está inicialmente vacía
tareas = []

# Lista con dos tareas
tareas = ["Lavar auto"]

# Mostrar todas las tareas
print(tareas)

# Agrega un elemento al final de la lista
tareas.append("Visitar médico")

# Elimina el primer elemento de la lista
tareas.pop(0)

# Muestra un elemento de la lista a la vez
for tarea in tareas:
    print(tarea)
    
# Elimina el último elemento de la lista
tareas.pop(len(tareas) - 1)

if len(tareas) == 0:
    print("La lista está vacía")
else:
    print(f"La lista contiene {len(tareas)} elementos")
    
print("¡Todas las tareas completadas!")