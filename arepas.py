print("Arepas Din�micas :) 
")

# Obtenemos los ingredientes del usuario y los convertimos a n�meros enteros

agua = input("Ingresa la cantidad de agua: (En Tazas) ")

harina = input("Ingresa la cantidad de harina de ma�z: (En Tazas) ")

sal = input("Ingresa la cantidad de sal: (En cucharaditas) ")

aceite = input("Ingresa la cantidad de aceite: (En cucharaditas) ")))


agua = int(agua)
harina = int(harina)
sal = int(sal)
aceite = int(aceite)

sal = sal / 48
aceite = aceite / 16

print(type(agua),type(harina),type(sal),type(aceite))


# Calculamos el volumen en el bol
bol = agua + harina + sal
print("El bol tiene", bol, "masa")

# calculamos con una medida estandar de las tazas que es 150gr por taza
foo = agua + harina + sal * 1.5
print("El bol tiene masa (gramos)", foo, "masa")

# Calculamos el volumen en el budare
budare = bol + aceite
print("En el budare hay", budare, "masa")

# Consideramos la p�rdida de masa al cocinar
budare *= 0.9
print("Despu�s de cocinar, en el budare quedan", budare, "masa")

# El volumen en el plato es el mismo que en el budare
plato = budare
print("El plato tiene", plato, "masa")
