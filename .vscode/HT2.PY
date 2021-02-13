print("================ EJERCICIO 1 =======================")
passcon = "contraseña"
num = str(input("Ingrese una contraseña: "))

if  num == passcon.lower():
    print(passcon)
else:
    print("No coincide la contrseña")       


print("=============== FIN EJERCICIO 1 =====================")
print(" ")

print("================ EJERCICIO 2 =======================")

nombre = input("Ingrese su nombre: ")
gemero = input("¿Cuál se su sexo (M o H)  ?")

if gemero == "M":
    if nombre.lower() < "m" :
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"        
print("Tu grupo es: " + grupo)