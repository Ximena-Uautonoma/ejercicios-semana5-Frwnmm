'''Registro de asistencia diaria
En una oficina se registra la asistencia hasta que el trabajador ingresa 0.
Solicita repetidamente:
1 si asistió
0 para terminar
Al final, muestra cuántos días asistió.'''

sum= 0
i = 1
while i == 1:
    sum= sum + i
    i = int(input("Ya es otro dia, 1 si asististe, 0 si no asisitiste: "))
    print("Hoy asististe, has asistido",sum, "dias")