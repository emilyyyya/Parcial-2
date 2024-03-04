from Estrella import Estrella
from Galaxia import imprimir_informacion, calcular_y_mostrar_distancias

def main():
    estrella_A = Estrella("Estrella A", 2, 3, 1)
    estrella_B = Estrella("Estrella B", 4, 4, 4)
    estrella_C = Estrella("Estrella C", -3, -1, 0)

    imprimir_informacion(estrella_A)
    imprimir_informacion(estrella_B)
    imprimir_informacion(estrella_C)

    calcular_y_mostrar_distancias(estrella_A, estrella_B)
    calcular_y_mostrar_distancias(estrella_B, estrella_C)
    calcular_y_mostrar_distancias(estrella_A, estrella_C)

    origen = Estrella("Origen")
    estrellas = [estrella_A, estrella_B, estrella_C]
    estrella_mas_lejana = max(estrellas, key=lambda estrella: estrella.distancia(origen))
    print(f"La estrella más lejana del origen es {estrella_mas_lejana.nombre} con una distancia de {estrella_mas_lejana.distancia(origen):.2f}")

if __name__ == "__main__":
    main()
    