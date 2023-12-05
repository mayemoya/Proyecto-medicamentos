"""En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y 
asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de salud y 
bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura por enfermedades no transmisibles mediante la prevención
y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la entrega de 2 tipos de medicamentos en una IPS 
para el tratamiento y prevención de la hipotensión y la hipertensión, en pos del mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe recibir como entrada la cantidad de existencias del medicamento 1 seguido de la cantidad de existencias 
del medicamento 2. Luego se deberán leer la información de la presión sistólica y la presión diastólica de múltiples pacientes y 
realizar la deducción de los medicamentos entregados hasta que se acaben o se deban existencias de uno de los 2 medicamentos.
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


Si no se encuentra la categoría del paciente el registro cuenta, pero no se entrega ningún tipo de medicamento.

Finalmente, se debe mostrar la cantidad de pacientes atendidos, la cantidad de pacientes a los que se les hizo entrega del 
medicamento 1 junto al porcentaje de estos respecto al total de pacientes atendidos formateado a 2 cifras decimales y la 
cantidad de pacientes a los que se les hizo entrega del medicamento 2 junto al porcentaje de estos respecto al total de 
pacientes atendidos formateado a 2 cifras decimales.
Además, si no se entregan medicamentos se debe mostrar que el total de pacientes atendidos, pacientes a los que se les hizo 
entrega del medicamento 1 y pacientes a los que se les hizo entrega del medicamento 2 es 0 y sus porcentajes correspondientes son 0.00%.
"""
a = int(input("Cantidad de existencias del medicamento 1: "))
b = int(input("Cantidad de existencias del medicamento 2: "))

pacientes = 0
med1 = 0
med2 = 0

while a > 1 and b > 1:
    c = int(input("Presion sistolica: "))
    d = int(input("Presion diastolica: "))
    if (c < 72) and (d < 65):
        pacientes += 1
        b -= 4
        med2 += 1
    elif (c >= 72) and (c < 107) and (d >= 65) and (d < 73):
        med1 += 0
        pacientes += 1
    elif (c >= 107) and (c < 124) and (d >= 73) and (d < 81):
        med1 += 0
        pacientes += 1
    elif (c >= 124) and (c < 138) and (d >= 81) and (d < 93):
        a -= 2
        med1 += 1
        pacientes += 1
    elif (c >= 138) and (c < 156) and (d >= 93) and (d < 102):
        a -= 4
        med1 += 1
        pacientes += 1
    elif (c >= 156) and (c < 175) and (d >= 102) and (d < 114):
        a -= 8
        med1 += 1
        pacientes += 1
    elif (c >= 175) and (d >= 114):
        a -= 16
        med1 += 1
        pacientes += 1
    elif (c >= 136) and (d < 92):
        a -= 12
        med1 += 1
        pacientes += 1
    else:
        pacientes +=1
if (a > 0) or (b > 0):
    porcm1=(med1*100)/pacientes
    porcm2=(med2*100)/pacientes
    print("",pacientes)
    print("",med1,"",f"{porcm1:.2f}","%")
    print("",med2,"",f"{porcm2:.2f}","%")
else:
    print(pacientes)
    print(med1, "0.00%")
    print(med2, "0.00%")