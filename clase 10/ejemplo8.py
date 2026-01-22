def celsios_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

temperatura_celsius = 100
print(f"{temperatura_celsius}°C son {celsios_a_fahrenheit(temperatura_celsius)}°F")

b=10
h=5
print(f"El área del triángulo de base {b} y altura {h} es {area_triangulo(b, h)}")