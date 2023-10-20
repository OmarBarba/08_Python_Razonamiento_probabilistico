# Definir las probabilidades
P_A = 0.3
P_B_dado_A = 0.7
P_C_dado_A = 0.4
P_B_dado_no_A = 0.2
P_C_dado_no_A = 0.6

# Definir evidencia
evidencia = {'B': 1, 'C': 0}

# Función para realizar el manto de eliminación de variables
def eliminacion_de_variables(probabilidades, evidencia):
    # Crear una lista de variables no observadas
    variables_no_observadas = [variable for variable in probabilidades.keys() if variable not in evidencia]
    
    # Inicializar la probabilidad conjunta
    probabilidad_conjunta = 1.0
    
    # Iterar sobre las variables no observadas
    for variable in variables_no_observadas:
        probabilidad_conjunta *= sum(probabilidades[variable][valor] for valor in [0, 1])
    
    return probabilidad_conjunta

# Calcular la probabilidad P(A|B=1, C=0) utilizando el manto de eliminación de variables
probabilidades = {
    'A': {0: P_A, 1: 1 - P_A},
    'B': {1: P_B_dado_A, 0: P_B_dado_no_A},
    'C': {1: P_C_dado_A, 0: P_C_dado_no_A}
}

probabilidad_A_dado_evidencia = eliminacion_de_variables(probabilidades, evidencia)

print(f"P(A|B=1, C=0) = {probabilidad_A_dado_evidencia:.2f}")
