"""tabla = int(input("tablas del: "))
for i in range(1,11):
    print(tabla, "x", i, "=", tabla*i)
    i = 1"""
    
j = 1
while j <= 11:
    i = 1
    print("tablas del", j)
    while i <=11:
        print (j, "x", i, "=", j*i)
        i += 1
    j += 1
    print("")