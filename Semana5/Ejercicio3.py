'''Cajero automático: validación de retiro
Un cajero permite retirar solo montos mayores a 0 y múltiplos de 10.
Solicita el monto hasta que sea válido y luego muestra "Retiro exitoso".'''
entrar=0
while(entrar==0):
    a = int(input("Ingresa el monto que quieres retirar de este cajero: "))
    if (a % 10 == 0):
        print("Retiro exitoso")
    else:
        print("No es valido para el retiro, este cajero solo permite retiros multiplos de 10")
    entrar= int(input("Ingresa 0 para retirar mas dinero, 1 para salir: "))
    if entrar == 1:
        print("Adios")