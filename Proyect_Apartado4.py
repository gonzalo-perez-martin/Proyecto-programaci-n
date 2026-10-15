import numpy as np

#Constantes del modelo
GAMMA = 1.4
R = 287.0
Mach_Cr = 1.2

#Datos atmósfera estándar
h_atm = np.array([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000])
T_atm = np.array([288.15, 275.15, 262.15, 249.15, 236.15, 223.15, 216.65, 216.65])

#t es un entero o un vector, la función devuelve un entero o un vector de la misma forma que t. 

def V_vuelo(t: float | np.ndarray) -> float | np.ndarray:     #define la función V_vuelo que calcula la velocidad de vuelo en función del tiempo t.
    return 800 * np.sin(np.pi * t / 60) * np.exp(-0.02 * t)   #valor de la velocidad de vuelo.

def Temp(t: float | np.ndarray) -> float | np.ndarray:        #Define la función Temp que calcula la temperatura en función del tiempo t.
    return np.interp(300 * t, h_atm, T_atm)                   #Interpola la temperatura en función de la altitud (300 * t) utilizando los arrays h_atm y T_atm. Devuelve la temperatura correspondiente a la altitud calculada.

def a_sonido(t: float | np.ndarray) -> float | np.ndarray:    #define la función a_sonido que calcula la velocidad del sonido en función del tiempo t.
    return np.sqrt(GAMMA * R * Temp(t))                       #ecuación para calcular la velocidad del sonido a partir de la temperatura. Raíz cuadrada de (Gamma*R*Temp(T)).

def Mach(t: float | np.ndarray) -> float | np.ndarray:        #define la función Mach que calcula el número de Mach en función del tiempo t.
    return V_vuelo(t) / a_sonido(t)                           #El número de Mach se obtiene dividiendo la velocidad de vuelo V_vuelo(t) por la velocidad del sonido a_sonido(t).

t_vuelo = np.linspace(0.0, 60.0, 1200)           #Crea un array de 1200 elementos que van desde 0 a 60 segundos, con un paso de 0.05 segundos entre cada elemento. Este array representa los tiempos de vuelo analizados.
mach_analizados = Mach(t_vuelo)                  #Calcula el Mach correspondiente a cada tiempo en t_vuelo utilizando la función Mach definida anteriormente. El resultado es un array de Machs correspondientes a cada tiempo analizado.

i= np.argmax (mach_analizados >= Mach_Cr)                                                 #np.argmax compara los valores de mach_analizados con Mach_Cr
if mach_analizados[i] < Mach_Cr:                                                          #si no halla ninguno igual al Mach crítico devuelve un 0 y procede a la siguiente línea
    raise ValueError("El cohete no alcanza el Mach crítico en el intervalo analizado")    #Raise detiene el programa mostrando un error con el siguiente mensaje si el Mach crítico no ocurrió entre 0 y 60 segundos.

t_c = np.interp(Mach_Cr, mach_analizados[i-1:i+1], t_vuelo[i-1:i+1])                      #Se define t_c como el tiempo en el cual el cohete alcanza el mach crítico.
print (f"El cohete alcanza Mach {Mach_Cr} crítico por primera vez a los {t_c:.4f} s")     #Se seleccionan las posiciones i-1 e i para interpolar el tiempo correspondiente al Mach crítico
                                                                                          # mach_analizados analiza los Machs cercanos a 1.2
                                                                                          #t_vuelo obtiene los tiempos correspondientes a esos Machs cercanos.
                                                                                          #la función np.interp realiza la interpolación lineal para encontrar el tiempo t_c en el que se alcanza el Mach crítico Mach_Cr.
