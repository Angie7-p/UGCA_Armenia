"""i = 1
while i <= 10:
    print (i) 
    i = i + 1 """

"""tabla= int(input("Cual tabla desea: "))
i = 1
while i <= 10:
    print (tabla, "x" ,i, "=", tabla*i)
    i += 1"""

"""i = 1
while i <=100:
    print (i/7)
    i /= 7"""
"""
i = 1
divisible = int(input("cual quieres de divisible: "))
while i <= 100:
    if i%divisible == 0:
        print(i)
    i += 1"""

"""totalcompra = 0
opcion = 0
while opcion != 5:

    input ("RESTAURANTE TRIQUI TRAQUE")
    print ("1. PIZZA - $10000")
    print ("2. PERRO - $12000")
    print ("3. HAMBURGUESA -$18000")
    print ("4. SALCHIPAPA -$14000")
    print ("5. TERMINAR")
    opcion = int(input("ingrese su opción: "))
    if opcion == 1:
        totalcompra += 10000
    elif opcion == 2:
        totalcompra += 12000
    elif opcion == 3:
        totalcompra += 18000
    elif opcion == 4:
        totalcompra += 14000

print ("el valor de su compra es: ")
sbt = int(input("numero de platillos: " * totalcompra))
opcion = int(input("La cantidad de platillos es: "))
print("El total de su compra es: ", sbt)"""

valorfactura = 0
opcion = 0
menu = """ESTAURANTE TRIQUI TRAQUE5
1. PIZZA - $10000
2. PERRO - $12000
3. HAMBURGUESA -$18000
4. SALCHIPAPA -$14000
5. TERMINAR """
print (menu)

while opcion != 5:
    opcion = int(input ("elija su opcion"))
    if opcion == 1:
        valorfactura += 10000
    elif opcion == 2:
        valorfactura += 12000
    elif opcion == 3:
        valorfactura += 18000
    elif opcion == 4:
        valorfactura += 14000

print ("el valor de su factura es", valorfactura)

sbt = ( opcion * valorfactura)
opcion = int(input("La cantidad de platillos es: "))
print("El total de su compra es: ", sbt)