def imprimir_informacion(estrella):
    print(estrella)
    print(f"Galaxia: {estrella.galaxia()}")

def calcular_y_mostrar_distancias(estrella1, estrella2):
    distancia = estrella1.distancia(estrella2)
    print(f"Distancia entre {estrella1.nombre} y {estrella2.nombre}: {distancia:.2f}")
