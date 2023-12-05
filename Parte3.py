"""En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y 
asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de salud y 
bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura por enfermedades no transmisibles mediante la prevención
y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la programar la entrega de existencias de un tipo 
de medicamento en varias sucursales de una IPS para el tratamiento y prevención de la hipotensión y la hipertensión, en pos del 
mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe recibir como entrada la cantidad de sucursales (n) para la entrega de medicamentos seguido de la 
cantidad total de pacientes a atender (m), si la cantidad de sucursales es menor a 1 se debe leer nuevamente ambos valores 
hasta que se ingrese un n válido. Luego, para las n sucursales (numeradas de 1 a n) se debe leer la cantidad de existencias 
actuales del medicamento y esta debe ser mayor o igual a 1, y en caso de que no se cumpla se debe leer valores hasta que se 
ingrese uno válido. Finalmente, para los m pacientes se debe leer el número de la sucursal donde será atendido, seguido de 
información de las presiones sistólica y diastólica del mismo.
Los rangos de valores de presión, así como su categoría y la cantidad y tipo de medicamento entregado se listan en la siguiente tabla: 

Presión Sistólica       Presión Diastólica      Categoría                           Tipo de Medicamento     Número de Dosis
< 72                    < 65                    Hipotension                         2                       4
[72 - 107)              [65 - 73)               Optima                              Ninguno                 0
[107 - 124)             [73 - 81)               Normal                              Ninguno                 0
[124 - 138)             [81 - 93)               Prehipertension                     1                       2
[138 - 156)             [93 - 102)              HTA Grado 1                         1                       4
[156 - 175)             [102 - 114)             HTA Grado 2                         1                       8
≥ 175                   ≥ 114                   HTA Grado 3                         1                       16
≥ 136                   < 92                    Hipertension Sistolica Aislada      1                       12


Si no se encuentra la categoría del paciente o la sucursal donde será atendido el paciente no es válida, no se programa la entrega 
ninguna existencia del medicamento.

El programa debe mostrar por pantalla el número de la sucursal con la menor cantidad de existencias, luego de realizar 
la entrega de las mismas, seguido de la cantidad antes mencionada. Luego, en una nueva línea se debe mostrar el número de 
la sucursal con la mayor cantidad de existencias, luego de realizar la entrega de las mismas, seguido de la cantidad antes 
mencionada. Finalmente, para cada una de las sucursales (en orden ascendente por número y en líneas distintas) se debe mostrar 
su número seguido de la proporción porcentual de las existencias del medicamento programadas para entrega respecto a la cantidad 
de existencias actuales del medicamento en la sucursal correspondiente, formateado a 2 cifras decimales y separado por espacio.
Si hay más de una sucursal con iguales cantidades mínimas o máximas, se debe mostrar la que tenga menor número.
"""
mensaje = input()
lista = mensaje.split(" ")
n = int (lista[0])
m = int (lista[1])

lista = []
while (n < 1):
    mensaje = input()
    lista = mensaje.split(" ")
    n = int (lista[0])
    lista.append(n)
    m = int (lista[1])

existencias = []
medicamentos = []
for i in range (n):
    med = int(input("Ingrese la cantidad de medicamentos: "))
    existencias.append(med)
    medicamentos.append(med)

while (med < 1):
    med = int(input("Ingrese la cantidad de medicamentos: "))
    existencias.append(med)
    medicamentos.append(med)

for i in range (m):
    mens = input()
    lista2 = mens.split(" ")
    pac = int (lista2[0])
    presis = int (lista2[1])
    predias = int (lista2[2])
    if (presis < 72) and (predias < 65):
        existencias [pac-1]= existencias [pac-1] - 4
    elif (presis >= 72) and (presis < 107) and (predias >= 65) and (predias < 73):
        existencias [pac-1]= existencias [pac-1] - 0
    elif (presis >= 107) and (presis < 124) and (predias >= 73) and (predias < 81):
        existencias [pac-1]= existencias [pac-1] - 0
    elif (presis >= 124) and (presis < 138) and (predias >= 81) and (predias < 93):
        existencias [pac-1]= existencias [pac-1] - 2
    elif (presis >= 138) and (presis < 156) and (predias >= 93) and (predias < 102):
        existencias [pac-1]= existencias [pac-1] - 4
    elif (presis >= 156) and (presis < 175) and (predias >= 102) and (predias < 114):
        existencias [pac-1]= existencias [pac-1] - 8
    elif (presis >= 175) and (predias >= 114):
        existencias [pac-1]= existencias [pac-1] - 16
    elif (presis >= 136) and (predias < 92):
        existencias [pac-1]= existencias [pac-1] - 12
    else:
        existencias [pac-1]= existencias [pac-1] - 0

mini = existencias[0]
sucmenor = 1
for i in range (len(existencias)):
    if mini > existencias[i]:
        mini = existencias[i]
        sucmenor = i + 1 
print(sucmenor, mini)

maxi = existencias[0]
sucmayor = 1
for i in range (len(existencias)):
    if maxi < existencias[i]:
        maxi = existencias[i]
        sucmayor = i + 1 
print(sucmayor, maxi)

for i in range (len(existencias)):
    div = (existencias[i]*100)/medicamentos[i]
    real = 100 - div
    print( i+1,f"{real:.2f}","%")