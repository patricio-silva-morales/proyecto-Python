votos = ["Juan", "Ana", "Marcela", "Juan", "Ana", "Ana", "Ana", "María", "Juan", "Felipe", "Sofía", "María", "Ana", "Juan", "Ana"]

candidatos_unicos = set(votos)
tupla_candidatos = tuple(candidatos_unicos)
print("Candidatos únicos:", tupla_candidatos)

# Creo diccionario vacío
conteo = {}

for candidato in votos:
    if candidato in conteo:
        conteo[candidato] += 1
    else:
        conteo[candidato] = 1

print("Votos válidos:", len(votos))

lista_ordenable = []
for nombre in conteo:
    lista_ordenable.append([conteo[nombre], nombre])

# Ordeno descendentemente la lista
lista_ordenable.sort(reverse=True)

print("Ranking de candidatos más votados:")
print(lista_ordenable[0])
print(lista_ordenable[1])
print(lista_ordenable[2])