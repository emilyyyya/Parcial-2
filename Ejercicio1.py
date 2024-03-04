import math

class Estrella:
    def __init__(self, nombre, x=0, y=0, z=0):
        """
        Constructor de la clase Estrella.

        :param nombre: Nombre de la estrella.
        :param x: Coordenada x en el espacio tridimensional.
        :param y: Coordenada y en el espacio tridimensional.
        :param z: Coordenada z en el espacio tridimensional.
        """
        self.nombre = nombre
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Método para obtener la representación en cadena de la estrella.

        :return: Cadena que representa la estrella.
        """
        return f"{self.nombre} en ({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        """
        Método para determinar la galaxia en la que podría estar ubicada la estrella.

        :return: Nombre de la galaxia.
        """
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Andromeda"
        elif self.x < 0 and self.y < 0 and self.z < 0:
            return "Galaxia Vía Láctea"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        """
        Método para calcular la distancia entre dos estrellas en el espacio 3D.

        :param otra_estrella: Otra instancia de la clase Estrella.
        :return: Distancia entre las dos estrellas.
        """
        dx = self.x - otra_estrella.x
        dy = self.y - otra_estrella.y
        dz = self.z - otra_estrella.z
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

def imprimir_informacion(estrella):
    """
    Función para imprimir información de una estrella.

    :param estrella: Instancia de la clase Estrella.
    """
    print(estrella)
    print(f"Galaxia: {estrella.galaxia()}")

def calcular_y_mostrar_distancias(estrella1, estrella2):
    """
    Función para calcular y mostrar la distancia entre dos estrellas.

    :param estrella1: Primera instancia de la clase Estrella.
    :param estrella2: Segunda instancia de la clase Estrella.
    """
    distancia = estrella1.distancia(estrella2)
    print(f"Distancia entre {estrella1.nombre} y {estrella2.nombre}: {distancia:.2f}")

def main():
    # Experimentación
    estrella_A = Estrella("Estrella A", 2, 3, 1)
    estrella_B = Estrella("Estrella B", 4, 4, 4)
    estrella_C = Estrella("Estrella C", -3, -1, 0)

    # Imprimir información de las estrellas y sus galaxias
    imprimir_informacion(estrella_A)
    imprimir_informacion(estrella_B)
    imprimir_informacion(estrella_C)

    # Calcular y mostrar distancias entre estrellas
    calcular_y_mostrar_distancias(estrella_A, estrella_B)
    calcular_y_mostrar_distancias(estrella_B, estrella_C)
    calcular_y_mostrar_distancias(estrella_A, estrella_C)

    # Encontrar la estrella más lejana del origen y mostrar información
    origen = Estrella("Origen")
    estrellas = [estrella_A, estrella_B, estrella_C]
    estrella_mas_lejana = max(estrellas, key=lambda estrella: estrella.distancia(origen))
    print(f"La estrella más lejana del origen es {estrella_mas_lejana.nombre} con una distancia de {estrella_mas_lejana.distancia(origen):.2f}")

if __name__ == "__main__":
    main()
