# Proyecto-medicamentos
Proyecto realizado para mision TIC 2021
En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es el de salud y bienestar y una de sus metas busca reducir en un tercio la mortalidad prematura por enfermedades no transmisibles mediante la prevención y el tratamiento.
Debido a esto, el ministerio de salud desea que usted construya un sistema para la detección temprana de una enfermedad en específico, siendo estas la hipertensión y la hipotensión, en pos del mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe recibir como entrada los datos de la presión sistólica y la presión diastólica de un paciente y muestre por pantalla la categoría en la que se encuentra la presión del paciente, así como el tipo de alerta que se genera dependiendo de la categoría mencionada previamente.
Los rangos de valores de presión, así como su categoría y alerta se listan en la siguiente tabla:
Presión Sistólica      Presión Diastólica      Categoría                         Alerta
< 72                    < 65                   Hipotension                       Amarilla      
[72 - 107)              [65 - 73)              Optima                            Verde
[107 - 124)             [73 - 81)              Normal                            Verde
[124 - 138)             [81 - 93)              Prehipertension                   Amarilla
[138 - 156)             [93 - 102)             HTA Grado 1                       Naranja
[156 - 175)             [102 - 114)            HTA Grado 2                       Roja
≥ 175                   ≥ 114                  HTA Grado 3                       Roja
≥ 136                   < 92                   Hipertension Sistolica Aislada    Naranja

Además, para cualquier combinación no válida de los valores de ambas presiones se debe mostrar el mensaje “No se puede determinar la categoria”, así como una alerta de color gris. 
