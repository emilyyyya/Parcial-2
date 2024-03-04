import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def galaxia(self):
        # Implementa la lógica para determinar la galaxia
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Vía Láctea"
        elif self.x < 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia de Andrómeda"
        elif self.x >= 0 and self.y < 0 and self.z >= 0:
            return "Galaxia del Triángulo"
        elif self.x >= 0 and self.y >= 0 and self.z < 0:
            return "Galaxia del Cigarro"
        else:
            return "Galaxia Desconocida"
    
    def distancia(self, otra_estrella):
        # Implementa el cálculo de la distancia
        distancia_cuadrada = (self.x - otra_estrella.x)**2 + (self.y - otra_estrella.y)**2 + (self.z - otra_estrella.z)**2
        distancia = math.sqrt(distancia_cuadrada)
        return distancia

def main():
    # Crea las estrellas
    estrella_A = Estrella(2, 3, 1)
    estrella_B = Estrella(4, 4, 4)
    estrella_C = Estrella(-3, -1, 0)
    
    # Imprime las estrellas por pantalla
    print("Estrella A:", estrella_A, "- Galaxia:", estrella_A.galaxia())
    print("Estrella B:", estrella_B, "- Galaxia:", estrella_B.galaxia())
    print("Estrella C:", estrella_C, "- Galaxia:", estrella_C.galaxia())
    
    # Calcula y muestra la distancia entre las estrellas A y B, y entre B y C
    distancia_AB = estrella_A.distancia(estrella_B)
    distancia_BC = estrella_B.distancia(estrella_C)
    print("Distancia entre A y B:", distancia_AB)
    print("Distancia entre B y C:", distancia_BC)
    
    # Encuentra qué estrella está más lejos del origen
    distancias_al_origen = {
        "A": estrella_A.distancia(Estrella()),
        "B": estrella_B.distancia(Estrella()),
        "C": estrella_C.distancia(Estrella())
    }
    estrella_mas_lejana = max(distancias_al_origen, key=distancias_al_origen.get)
    print(f"La estrella más lejana del origen es la {estrella_mas_lejana}.")

if __name__ == "__main__":
    main()
