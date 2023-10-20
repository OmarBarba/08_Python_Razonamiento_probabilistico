##############################################
#############Muestreo directo#################
##############################################

import random

# Número de muestras
n_muestras = 10000

# Inicializar el contador de números pares
conteo_pares = 0

# Realizar el muestreo directo
for _ in range(n_muestras):
    muestra = random.randint(1, 6)
    if muestra % 2 == 0:
        conteo_pares += 1

# Calcular la probabilidad de obtener un número par
probabilidad_par = conteo_pares / n_muestras

print(f"Probabilidad de obtener un número par: {probabilidad_par:.4f}")

##############################################
############# Muestreo rechazo#################
##############################################

# Definir la distribución de interés (en este caso, una distribución uniforme)
rango_inicio = 20
rango_fin = 30
# Inicializar el contador de muestras en el rango
muestras_en_rango = 0
# Realizar el muestreo por rechazo
for _ in range(n_muestras):
    muestra = random.randint(1, 100)  # Supongamos que estamos muestreando entre 1 y 100
    if rango_inicio <= muestra <= rango_fin:
        muestras_en_rango += 1

# Calcular la probabilidad de que una muestra esté en el rango
probabilidad_en_rango = muestras_en_rango / n_muestras

print(f"Probabilidad de que una muestra esté en el rango [{rango_inicio}, {rango_fin}]: {probabilidad_en_rango:.4f}")