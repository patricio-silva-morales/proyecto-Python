# Prueba de uso de break en while
contador = 1

while contador <= 10:
    if contador == 5:
        break
    
    print(contador)
    
    contador += 1

# Prueba de uso de continue en while
contador = 0

while contador < 10:
    contador += 1
    
    if contador == 3:
        continue
        
    print(contador)  
    