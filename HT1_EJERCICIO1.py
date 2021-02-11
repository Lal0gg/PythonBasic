print("================ EJERCICIO 1 =======================")
num = int(input("Digite un número entero: "))
for i in range(num +1):
    print("*"*i)

print("=============== FIN EJERCICIO 1 =====================")
print(" ")

print("================ EJERCICIO 2 =======================")
nume = int(input("Ingrese un número entero: "))

if nume > 1:
    cotado = 0
    for i in range(2,nume):
        resi=nume%i

        if resi==0:
            cotado+=1
    if cotado==0:
        print("El numero es primo ")
    else:
        print("El numero no es primo ")    

else:
    print("El numero no es primo ") 
print("=============== FIN EJERCICIO 2 =====================")
