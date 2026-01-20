# Lista tareas está inicialmente vacía
tareas = []

# Agrega un elemento al final de la lista
tareas.append("Llamar a cliente")

# Agrega un elemento ANTES de la posición indicada
tareas.insert(0, "Revisar emails")

# Agrega un elemento ANTES de la posición indicada
tareas.insert(1, "Agendar reunión con equipo")

print(tareas)

# Elimina el elemento de la posición indicada 
# tareas.pop(2)

# Elimina el último elemento de la lista
tareas.pop(len(tareas) - 1)

print(tareas)
