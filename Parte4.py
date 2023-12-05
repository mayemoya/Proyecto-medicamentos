"""En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y 
asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de salud y 
bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura por enfermedades no transmisibles mediante la prevención
y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la programar la entrega de existencias de un tipo 
de medicamento en varias sucursales de una IPS para el tratamiento y prevención de la hipotensión y la hipertensión, en pos del 
mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe recibir como entrada la cantidad de sucursales (n) para la entrega de medicamentos seguido del número 
de diferentes tipos de medicamento (k) y de la cantidad total de pacientes a atender (m), si la cantidad de sucursales es menor a 1 
o si el número de diferentes tipos de medicamento es menor a 1 se debe leer nuevamente todos los valores previamente mencionados hasta 
que se ingresen un n y un k válidos. 
Luego, para las n sucursales (numeradas de 1 a n) se debe leer la cantidad de existencias actuales de todos los tipos de medicamentos 
en una línea. Finalmente, para los m pacientes se debe leer el número de la sucursal donde será atendido, seguido del tipo de 
medicamento solicitado y el número de existencias solicitadas del mismo, seguido de la información de las presiones sistólica y 
diastólica.
Los rangos de valores de presión, así como su categoría y si se programa o no la entrega de existencias se listan en la siguiente tabla: 
 

Presión Sistólica       Presión Diastólica      Categoría                           ¿Se le programa entrega?
< 72                    < 65                    Hipotension                         Si                       
[72 - 107)              [65 - 73)               Optima                              No                 
[107 - 124)             [73 - 81)               Normal                              No                 
[124 - 138)             [81 - 93)               Prehipertension                     Si                       
[138 - 156)             [93 - 102)              HTA Grado 1                         Si                       
[156 - 175)             [102 - 114)             HTA Grado 2                         Si                       
≥ 175                   ≥ 114                   HTA Grado 3                         Si                       
≥ 136                   < 92                    Hipertension Sistolica Aislada      Si                       


Si no se encuentra la categoría del paciente o la sucursal donde será atendido el paciente no es válida o el tipo de medicamento no 
es válido o la cantidad de dosis solicitadas es menor a 0, no se programa la entrega ninguna existencia del medicamento y el paciente 
tampoco se toma en cuenta en el conteo de pacientes por sucursal.

El programa debe mostrar por pantalla para cada una de las sucursales:
El número de la sucursal.
El número del tipo de medicamento con la menor cantidad de existencias luego de realizar la entrega de las existencias programadas, 
seguido de la cantidad antes mencionada.
El número del tipo de medicamento con la mayor cantidad de existencias luego de realizar la entrega de las existencias programadas, 
seguido de la cantidad antes mencionada.
La cantidad mínima, promedio y máxima de existencias programadas para entrega entre los k tipos de medicamento, formateado a 2 cifras 
decimales y separados por espacio.
El promedio de existencias programadas, independientemente del tipo, por paciente en la sucursal correspondiente, formateado a 2 cifras 
decimales y separados por espacio. Si la cantidad de pacientes atendidos en la sucursal es 0, el promedio debe ser 0.00.

Si hay más de un medicamento con iguales cantidades mínimas o máximas luego de hacer la entrega de las existencias programadas, se debe 
mostrar el que tenga el menor número. 

Finalmente, se debe mostrar:
El número de la sucursal con la menor cantidad de existencias programadas para entrega del medicamento de tipo 1, 
seguido de la cantidad antes mencionada.
El número de la sucursal con la mayor cantidad de existencias programadas para entrega del medicamento de tipo 1, 
seguido de la cantidad antes mencionada.

Si hay más de una sucursal con iguales cantidades mínimas o máximas de la cantidad de existencias programadas del medicamento de tipo 1,
se debe mostrar la que tenga menor número.

"""
mensaje = input()
lista = mensaje.split(" ")
n = int (lista[0])
k = int (lista[1])
m = int (lista[2])

lista = []
while (n < 1) or (k < 1):
    mensaje = input()
    lista = mensaje.split(" ")
    n = int (lista[0])
    k = int (lista[1])
    m = int (lista[2])
    lista.append(n)

existencias = []
medicamentos = []
for i in range (n):
    ese = input()
    lis = ese.split(" ")
    med = int(input("Ingrese la cantidad de medicamentos: ") (lis[0]))
    existencias.append(med)
    medicamentos.append(med)

for i in range (m):
    mens = input()
    lista2 = mens.split(" ")
    pac = int (lista2[0])
    medi = int (lista2[1])
    exis = int (lista2[2])
    presis = int (lista2[3])
    predias = int (lista2[4])
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

print(pac)

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