# Probabilidades individuales
P_A = 0.3  # P(A)
P_B_dado_A = 0.6  # P(B|A)
P_C_dado_A_B = 0.7  # P(C|A, B)

# Calcular la probabilidad conjunta P(A, B, C) usando la regla de la cadena
P_A_y_B_y_C = P_A * P_B_dado_A * P_C_dado_A_B

print("P(A, B, C) =", P_A_y_B_y_C)
