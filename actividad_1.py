import numpy as np
import matplotlib.pyplot as plt

def graficar_polinomios(*polinomios):
    """
    Función para graficar un número arbitrario de polinomios de la forma ax^n.
    
    Parámetros:
    - polinomios: Tuplas con (a, n) donde 'a' es el coeficiente y 'n' es el exponente.
    """
    x = np.linspace(-10, 10, 400)  # Rango de valores de X

    plt.figure(figsize=(8, 6))  # Definir tamaño de la gráfica

    for a, n in polinomios:
        y = a * x**n  # Calcula el polinomio ax^n
        plt.plot(x, y, label=f'{a}x^{n}')  # Agrega la línea al gráfico

    plt.axhline(0, color='black', linewidth=0.8)  # Línea horizontal en Y=0
    plt.axvline(0, color='black', linewidth=0.8)  # Línea vertical en X=0
    plt.grid(True, linestyle='--', alpha=0.6)  # Agregar cuadrícula
    plt.legend()  # Mostrar leyenda
    plt.title("Gráfica de Polinomios")  # Título
    plt.xlabel("Eje X")  # Etiqueta X
    plt.ylabel("Eje Y")  # Etiqueta Y

    # <--- IMPORTANTE PARA MOSTRAR LA GRÁFICA
    plt.savefig("grafica.png")  # Guarda la imagen
    plt.show(block=True)  # Forzar la visualización de la gráfica

# Ejemplo de uso con tres polinomios
graficar_polinomios((1, 2), (-0.5, 3), (2, 1))

class LectorTXT:
    def __init__(self):
        self.ruta_static = "static/"

    def leer_txt(self):
        ruta_txt = "{}txt/instruccion_1.txt".format(self.ruta_static)
        with open(ruta_txt, "r", encoding="utf-8") as f:
            return f.read()

# Crear instancia de la clase y leer el archivo
lector = LectorTXT()
contenido = lector.leer_txt()
print("\nContenido del archivo:")
print(contenido)
