import numpy as np
# 1. Calibracion del sensor principal de empuje (Voltaje [V] vs Fuerza [kN])
voltaje_sensor = np.array([0.0, 1.25, 2.45, 3.80, 5.10])
fuerza_real = np.array([0.0, 15.2, 31.0, 48.5, 65.3])
# 2. Reacciones en la plataforma de lanzamiento (Coordenadas apoyos y pesos)
# Matriz de geometria estatica (distancias en m) para el balance de masas
matriz_estatica = np.array([
[1.0, 1.0, 1.0],
# Suma de fuerzas Z
[0.0, 1.5,-1.5],
# Momentos en X
[-2.0, 1.0, 1.0]
# Momentos en Y
])
vector_cargas = np.array([25000.0, 1500.0,-800.0]) # [N, Nm, Nm]
# 3. Datos de Atmosfera Estandar (Altitud [m], Temperatura [K], Presion [Pa])
h_atm = np.array([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000])
T_atm = np.array([288.15, 275.15, 262.15, 249.15, 236.15, 223.15, 216.65,
216.65])
P_atm = np.array([101325, 79501, 61660, 47217, 35651, 26499, 19399, 14170])
# 4. Telemetria de vuelo: Tiempo [s] y Velocidad [m/s]
t_vuelo = np.linspace(0, 60, 1200) # Muestreo a 20 Hz
# (Perfil simulado de velocidad de un cohete)
v_vuelo = 800 * np.sin(np.pi * t_vuelo / 60) * np.exp(-0.02 * t_vuelo)