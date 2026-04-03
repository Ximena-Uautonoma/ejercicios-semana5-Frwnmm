'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''
a = int(input("Ingresa un la temperatura actual en grados C y te dire si es fria, templada o calurosa: "))
if a <= 10:
    print("Afuera esta Frio")
elif a <= 25:
    print("Afuera esta Templado")
elif a > 25:
    print("Afuera esta soleado")
else:
    print("Ingresa un numero valido")