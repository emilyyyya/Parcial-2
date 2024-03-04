
def formatear_texto(texto_original):
    # Dividir el texto en una lista de líneas
    lineas = texto_original.split("#")

    # Iterar sobre cada línea y formatearla
    for i, linea in enumerate(lineas):
        if i == 0:
            # Capitalizar la primera letra de la primera línea
            lineas[i] = linea.capitalize() + "..."
        else:
            # Agregar el formato de diálogo para el resto de las líneas
            lineas[i] = "\n" + linea.capitalize() + " -" * (i != len(lineas) - 1) + "."

    # Unir las líneas formateadas en un solo texto
    texto_formateado = "".join(lineas)

    return texto_formateado

def main():
    # Solicitar al usuario que ingrese el texto en bruto
    texto_original = input("Ingrese el texto en bruto: ")

    # Formatear el texto
    texto_formateado = formatear_texto(texto_original)

    # Imprimir el texto formateado
    print(texto_formateado)

if __name__ == "__main__":
    main()
