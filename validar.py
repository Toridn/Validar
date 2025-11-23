def es_numero(texto):
    if texto == "":
        return False  
    
    for caracter in texto:
        if caracter < '0' or caracter > '9':
            return False  
    
    return True  


dato = input("Ingrese su edad: ")
 
while not es_numero(dato):
    print("ERROR: debe ingresar un número.")
    dato = input("Ingrese su edad nuevamente: ")
 
edad = int(dato)
print("Edad registrada:", edad)









# while True:

#     if es_numero(input("Ingrese un numero: ")):
#         print("El valor ingresado es numero puede continuar con el codigo")
#         break
#     else:
#         print("El valor ingresado no es un numero intente nuevamente")
#         continue


