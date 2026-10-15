from numpy import array, interp, linspace

t_vuelo = linspace(0, 60, 1200)

def altitude(t: float) -> float:
    return 300*t


h_atm = array([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000])
T_atm = array([288.15, 275.15, 262.15, 249.15, 236.15, 223.15, 216.65, 216.65])
# P_atm = array([101325, 79501, 61660, 47217, 35651, 26499, 19399, 14170])

h_flight = altitude(t_vuelo)
T_flight = interp(h_flight, h_atm, T_atm)

t = float(input("Type a number: "))
T = interp(altitude(t), h_atm, T_atm)
print("La temperatura tras ",t ," segundos es de ", T)