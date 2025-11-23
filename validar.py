def soloNumero(texto):
    if texto == "":
        return False  
    
    for caracter in texto:
        if caracter < '0' or caracter > '9':
            return False  
    
    return True  

def soloTexto(texto):
    if texto == "":
        return False  # No aceptar string vacío
    
    for c in texto:
        # Validar letras mayúsculas
        if c >= 'A' and c <= 'Z':
            continue
        
        # Validar letras minúsculas
        if c >= 'a' and c <= 'z':
            continue
        
        # Si no es letra, retorna False
        return False
    
    return True  # Todos los caracteres fueron letras

def validarRut(texto):
    if texto == "":
        return False  # No aceptar vacío

    for c in texto:
        # Validar números
        if c >= '0' and c <= '9':
            continue

        # Validar guion
        if c == '-':
            continue

        # Validar letra K (mayúscula o minúscula)
        if c == 'k' or c == 'K':
            continue

        # Si llega aquí, el caracter NO es permitido
        return False

    return True  # Todos los caracteres son válidos


dato = input("Ingrese su edad: ")
 
while not soloNumero(dato):
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


