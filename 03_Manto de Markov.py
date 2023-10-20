import numpy as np

# Matriz de transición (probabilidades de transición)
# Cada fila representa el estado actual y cada columna el estado siguiente.
# Ejemplo: P(A|A) = 0.7, P(A|B) = 0.2, P(A|C) = 0.1, y así sucesivamente.
matriz_transicion = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

# Estado inicial (probabilidades iniciales)
estado_inicial = np.array([0.4, 0.4, 0.2])

# Función para realizar inferencia en la cadena de Markov
def inferencia_markov(matriz_transicion, estado_inicial, pasos):
    estado_actual = estado_inicial
    for _ in range(pasos):
        estado_actual = np.dot(estado_actual, matriz_transicion)
    return estado_actual

# Realizar inferencia para 2 pasos
pasos = 2
resultado = inferencia_markov(matriz_transicion, estado_inicial, pasos)

print(f"Después de {pasos} pasos, las probabilidades de estado son:")
print("A:", resultado[0])
print("B:", resultado[1])
print("C:", resultado[2])
