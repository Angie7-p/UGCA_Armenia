genero = input("ingrese el genero f o m: ")
if genero == "f":
    print("MUJER")
if genero == "m":
    print("HOMBRE")
horastrabajadas = int(input ("horas trabajadas: "))
valorhora = int(input ("ingrese el valor por hora: "))
valorapagar = horastrabajadas * valorhora
if genero == "f" and valorapagar <=1500000:
    valorapagar += 200000
if genero == "m" and valorapagar <=1500000:
    valorapagar += 100000
if genero == "f" or "m" and valorapagar <=1500000 and valorapagar< 2000000:
    valorapagar += 50000
print (" usted a ganado", valorapagar)