# Número de caras observadas
n_caras_observadas = 6

# Número de cruces observadas
n_cruces_observados = 2

# Probabilidad a priori de obtener caras (antes de observar los datos)
probabilidad_priori_caras = 0.5

# Probabilidad a priori de obtener cruces
probabilidad_priori_cruces = 0.5

# Calcular la probabilidad de obtener caras en el próximo lanzamiento utilizando ponderación de verosimilitud
probabilidad_verosimilitud_caras = (n_caras_observadas / (n_caras_observadas + n_cruces_observados))

# Actualizar la probabilidad a priori utilizando la ponderación de verosimilitud
probabilidad_posterior_caras = (probabilidad_priori_caras * probabilidad_verosimilitud_caras)
probabilidad_posterior_cruces = (probabilidad_priori_cruces * (1 - probabilidad_verosimilitud_caras))

# Normalizar las probabilidades posteriores para que sumen 1
suma_probabilidades_posterior = probabilidad_posterior_caras + probabilidad_posterior_cruces
probabilidad_posterior_caras /= suma_probabilidades_posterior
probabilidad_posterior_cruces /= suma_probabilidades_posterior

print(f"Probabilidad de obtener caras en el próximo lanzamiento: {probabilidad_posterior_caras:.4f}")
