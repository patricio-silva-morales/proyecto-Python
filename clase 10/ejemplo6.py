calorias = [100, 305, 120, 200, 370, 165, 90, 400]

categorias = list(map(lambda x: "Snack liviano" if x < 150 else "Barrita energética" if x <= 300 else "Smoothie o batido", calorias))

print(categorias)

entrenamientos = list(filter(lambda x: x > 300, calorias))

print(entrenamientos)