"""En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y 
asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de salud y 
bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura por enfermedades no transmisibles mediante la prevención
y el tratamiento. Debido a esto, el ministerio de salud desea que usted construya un sistema para la detección temprana de una enfermedad
en específico, siendo estas la hipertensión y la hipotensión, en pos del mejoramiento de la calidad de vida de los ciudadanos. Para ello,
el sistema debe recibir como entrada los datos de la presión sistólica y la presión diastólica de un paciente y muestre por pantalla la
categoría en la que se encuentra la presión del paciente, así como el tipo de alerta que se genera dependiendo de la categoría mencionada
previamente. Los rangos de valores de presión, así como su categoría y alerta se listan en la siguiente tabla: 
Presión Sistólica       Presión Diastólica      Categoría                       Alerta 
< 72                    < 65                    Hipotension                     Amarilla
[72 - 107)              [65 - 73)               Optima                          Verde 
[107 - 124)             [73 - 81)               Normal                          Verde 
[124 - 138)             [81 - 93)               Prehipertension                 Amarilla 
[138 - 156)             [93 - 102)              HTA Grado 1                     Naranja 
[156 - 175)             [102 - 114)             HTA Grado 2                     Roja 
≥ 175                   ≥ 114                   HTA Grado 3                     Roja 
≥ 136                   < 92                    Hipertension Sistolica Aislada  Naranja

Además, para cualquier combinación no válida de los valores de ambas presiones se debe mostrar el mensaje 
“No se puede determinar la categoria”, así como una alerta de color gris."""

print("Presion del paciente ")
valor1 = int(input("Presion Sistolica: "))
valor2 = int(input("Presion Diastolica: "))

if (valor1 < 72) and (valor2 < 65):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria Hipotension Alerta Amarilla")
elif (valor1 >= 72) and (valor1 < 107) and (valor2 >= 65) and (valor2 < 73):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria Optima Alerta Verde")
elif (valor1 >= 107) and (valor1 < 124) and (valor2 >= 73) and (valor2 < 81):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria Normal Alerta Verde")
elif (valor1 >= 124) and (valor1 < 138) and (valor2 >= 81) and (valor2 < 93):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria Prehipertension Alerta Amarilla")
elif (valor1 >= 138) and (valor1 < 156) and (valor2 >= 93) and (valor2 < 102):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria HTA Grado 1 Alerta Naranja")
elif (valor1 >= 156) and (valor1 < 175) and (valor2 >= 102) and (valor2 < 114):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria HTA Grado 2 Alerta Roja")
elif (valor1 >= 175) and (valor2 >= 114):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria HTA Grado 3 Alerta Roja")
elif (valor1 >= 136) and (valor2 < 92):
  print("Su presion arterial es: ", valor1, " - ",valor2,". Categoria Hipertension Sistolica Aislada Alerta Naranja")
else:
  print("No se puede determinar la categoria Alerta Gris")