import os
import hashlib
import rsa

"""Lógica del programa"""

# Calcular el hash del texto.
def calcularHash(texto):
    textoConHash = hash(texto)
    return textoConHash

# Compresión del mensaje.
def comprimirMensaje(mensaje):
    print("Firmando mensaje...")

# Firmar el hash.
def firmarHash(texto):
    rsa.encrypt(texto) 

# Simular envío.
def simularEnvio():
    print("Se enviará el mensaje comprimido, la fimra y la clave pública.")
    info = ["Texto comprimido", "Firma", "clave pública"]

# Descomprimir y verificar firma.
def descomprimirMensaje(mensajeEncriptado, original):
    print("Descomprimiendo mensaje...")
    desencriptado = rsa.decrypt(mensajeEncriptado)
    if desencriptado == original:
        print("Texto validado.")
    else:
        print("Texto invalidado.")

# Mostrar si el mensaje es auténtico o no.


"""Interfaz del programa"""
detenerse = False
while detenerse == False:
    os.system("cls")
    print("Sistema de cifrado.")
    print("Ingrese la opción que requiera: ")
    print("1. Ingresar mensaje.")
    print("2. Calcular Hash FNV-1.")
    print("3. Comprimir mensaje.")
    print("4. Firmar el Hash con la clave privada.")
    print("5. Simular envío (mensaje comprimido + firma + clave pública).")
    print("6. Descomprimir y verificar firma (clave pública).")
    print("7. Mostrar si el mensaje es auténtico o alterado.")
    print("8. Salir.")
    opcion = int(input("Opción: "))

    if opcion == 1:
        os.system("cls")
        print("Ingrese el texto a guardar: ")
        textoAGuardar = input("Texto: ")
        input("Presione enter para continuar.")

    elif opcion == 2:
        os.system("cls")
        print("Se calculará el hash.")
        print(textoAGuardar)
        calcularHash(textoAGuardar)
        hashAlmacenado = calcularHash
        input("Presione enter para continuar.")

    elif opcion == 3:
        os.system("cls")
        print("")

        input("Presione enter para continuar.")

    elif opcion == 4: 
        os.system("cls")
        firmado = firmarHash(hashAlmacenado)
        input("Presione enter para continuar.")

    elif opcion == 5:
        os.system("cls")
        simularEnvio()
        input("Presione enter para continuar.")

    elif opcion == 6:
        os.system("cls")
        print("Se descomprimirá y verificará la firma.")
        descomprimirMensaje(firmado, textoAGuardar)
        input("Presione enter para continuar.")

    elif opcion == 7:
        os.system("cls")
        print("Verificando si el mensaje es auténtico o alterado")

        input("Presione enter para continuar.")

    elif opcion == 8:
        os.system("cls")
        print("Rodrigo Gabriel Pérez Vásquez, 1576224")

    else: 
        print("Seleccione una opción válida.")