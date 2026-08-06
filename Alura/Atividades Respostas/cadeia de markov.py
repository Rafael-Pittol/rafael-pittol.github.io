import numpy as np

# Definição dos estados do clima
states = ["Ensolarado", "Nublado", "Chuvoso"]

# Matriz de transição de estados
# As probabilidades em cada linha somam 1
transition_matrix = np.array([
    [0.8, 0.15, 0.05],  # Transições a partir de "Ensolarado"
    [0.2, 0.6, 0.2],    # Transições a partir de "Nublado"
    [0.25, 0.25, 0.5]   # Transições a partir de "Chuvoso"
])

# Validação: cada linha da matriz de transição deve somar 1
if not np.allclose(transition_matrix.sum(axis=1), 1.0):
    raise ValueError("Cada linha da matriz de transição deve somar 1.")

# Escolha do estado inicial
print("Estados disponíveis: Ensolarado, Nublado, Chuvoso")
initial_state = input("Escolha um estado inicial: ").strip().title()

# Número de dias a prever
num_days = 10

# Função para encontrar o índice de um estado
def get_state_index(state):
    return states.index(state)

# Função para prever o clima para os próximos dias
def predict_weather(initial_state, num_days):
    if initial_state not in states:
        raise ValueError(f"Estado inicial inválido: {initial_state}")
    if num_days < 1:
        raise ValueError("O número de dias deve ser maior ou igual a 1.")

    current_state = initial_state
    forecast = [current_state]

    for _ in range(num_days - 1):
        current_index = get_state_index(current_state)
        next_state_index = np.random.choice(
            len(states),
            p=transition_matrix[current_index]
        )
        current_state = states[next_state_index]
        forecast.append(current_state)

    return forecast

# Realizar a previsão
forecast = predict_weather(initial_state, num_days)

# Exibir a previsão
print(f"Estado inicial: {initial_state}")
print("Previsão para os próximos dias:")
for day, state in enumerate(forecast, start=1):
    print(f"Dia {day}: {state}")