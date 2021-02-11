print("================ EJERCICIO 1 =======================")
num = int(input("Digite un número entero: "))
#num es la variable que guarda el numero ingresado por el usuario
for i in range(num +1):
    print("*"*i)

print("=============== FIN EJERCICIO 1 =====================")
print(" ")

print("================ EJERCICIO 2 =======================")
nume = int(input("Ingrese un número entero: "))
#nume es la variable que guarda el numero ingresado por el usuario
if nume > 1:
    cotado = 0 #cotado es la variable que servirá de contador
    for i in range(2,nume):
        resi=nume%i
        #resi es la variable que guardará el residuo 
        #del numero que se ingresa

        if resi==0:

        # lo que hace la variable cotado es que aumentará cada vez que se
        # que es divisible un número
            cotado+=1
    if cotado==0:
       
        print("El numero es primo ")
    else:
        print("El numero no es primo ")    
        # por lo tanto cadav vez que la variable cotado se aumente mas de dos veces
        # por definición será un número que no e primo 
    

else:
    print("El numero no es primo ") 
print("=============== FIN EJERCICIO 2 =====================")
