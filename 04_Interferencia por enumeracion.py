# Definir las probabilidades
P_A = 0.3
P_B_dado_A = 0.7
P_C_dado_A = 0.4
P_B_dado_no_A = 0.2
P_C_dado_no_A = 0.6

# Definir evidencia
evidencia = {'B': 1, 'C': 0}

# Función para realizar inferencia por enumeración
def inferencia_por_enumeracion(probabilidades, evidencia):
    # Crear una lista de variables no observadas
    variables_no_observadas = [variable for variable in probabilidades.keys() if variable not in evidencia]
    
    probabilidad_total = 0
    for valor in [0, 1]:  # Para cada valor de la variable no observada
        evidencia_actualizada = evidencia.copy()
        for variable in variables_no_observadas:
            evidencia_actualizada[variable] = valor
        
        probabilidad_con_valor = 1
        for variable, valor in evidencia_actualizada.items():
            if variable in probabilidades:
                probabilidad_con_valor *= probabilidades[variable][valor]
        
        probabilidad_total += probabilidad_con_valor
    
    return probabilidad_total

# Calcular la probabilidad P(A|B=1, C=0)
probabilidades = {
    'A': {0: P_A, 1: 1 - P_A},
    'B': {1: P_B_dado_A, 0: P_B_dado_no_A},
    'C': {1: P_C_dado_A, 0: P_C_dado_no_A}
}

probabilidad_A_dado_evidencia = inferencia_por_enumeracion(probabilidades, evidencia)

print(f"P(A|B=1, C=0) = {probabilidad_A_dado_evidencia:.2f}")
