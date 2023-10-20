import random

# Matriz de transición
matriz_transicion = [
    [0.2, 0.6, 0.2],
    [0.3, 0.0, 0.7],
    [0.4, 0.3, 0.3]
]

# Estado inicial (por ejemplo, estado A)
estado_actual = 0  # A es el estado 0

# Número de pasos de Monte Carlo
n_pasos = 10

# Lista para almacenar la secuencia de estados
secuencia_estados = []

# Realizar el muestreo de Monte Carlo
for _ in range(n_pasos):
    secuencia_estados.append(estado_actual)
    transiciones_posibles = matriz_transicion[estado_actual]
    estado_actual = random.choices(range(len(transiciones_posibles)), weights=transiciones_posibles)[0]

# Imprimir la secuencia de estados
print("Secuencia de estados generada por Monte Carlo:")
print(secuencia_estados)
