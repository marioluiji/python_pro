import random

K = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

x = int(input("escribe la lonjitud de tu contraseña"))

characters = ""

for i in range(x):
    characters += random.choice(k)

print(characters)
