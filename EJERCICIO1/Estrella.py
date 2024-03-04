import math

class Estrella:
    def __init__(self, nombre, x=0, y=0, z=0):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.nombre} en ({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Andromeda"
        elif self.x < 0 and self.y < 0 and self.z < 0:
            return "Galaxia Vía Láctea"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        dx = self.x - otra_estrella.x
        dy = self.y - otra_estrella.y
        dz = self.z - otra_estrella.z
        return math.sqrt(dx**2 + dy**2 + dz**2)
    
    
