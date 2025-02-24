import numpy as np  # Para manejar números y cálculos matemáticos
import matplotlib.pyplot as plt  # Para graficar los polinomios
import json  # Para guardar los polinomios en un archivo JSON

def guardar_polinomios_json(polinomios, filename="polinomios.json"):
    """
    Guarda la lista de polinomios en un archivo JSON.
    """
    with open(filename, "w") as f:
        json.dump({"polinomios": polinomios}, f, indent=4)
def graficar_polinomios(*polinomios):
    """
    Grafica un número arbitrario de polinomios de la forma f(x) = ax^n.
    
    Parámetros:
    - *polinomios: Tuplas (a, n) donde 'a' es el coeficiente y 'n' el exponente.
    
    La función usa el operador * para recibir múltiples polinomios.
    """
    # Guardamos los polinomios en JSON
    guardar_polinomios_json(polinomios)

    # Definimos el rango de valores para x
    x = np.linspace(-10, 10, 400)  

    # Configuramos la gráfica
    plt.figure(figsize=(8, 6))  

    # Recorremos cada polinomio y lo graficamos
    for polinomio in polinomios:
        a, n = polinomio  # Extraemos los valores de a y n
        y = a * (x ** n)  # Calculamos la función y = ax^n
        plt.plot(x, y, label=f'f(x) = {a}x^{n}')  # Agregamos la leyenda

    # Configuración visual de la gráfica
    plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y=0
    plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x=0
    plt.legend()  # Mostramos la leyenda con las funciones
    plt.grid(True)  # Activamos la cuadrícula
    plt.title("Gráfica de Polinomios")  # Título
    plt.xlabel("x")  
    plt.ylabel("f(x)")  
    plt.show()  # Mostramos la gráfica

# Ejemplo de uso con tres polinomios
graficar_polinomios((1, 2), (-0.5, 3), (2, 1))
