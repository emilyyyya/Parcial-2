def magia_numerica(lista):
    # Hacemos una copia de la lista original para no modificarla
    lista_copia = lista.copy()
    
    # Eliminar elementos duplicados
    lista_copia = list(set(lista_copia))
    
    # Ordenar la lista de mayor a menor
    lista_copia.sort(reverse=True)
    
    # Eliminar todos los números impares
    lista_copia = [num for num in lista_copia if num % 2 == 0]
    
    # Sumar todos los números que quedan
    suma = sum(lista_copia)
    
    # Colocar la suma como el primer elemento de la lista
    lista_copia.insert(0, suma)
    
    return lista_copia

def verificar_magia(lista):
    # Verificar si la suma de todos los números a partir del segundo elemento
    # es igual al primer número de la lista
    suma_restante = sum(lista[1:])
    return lista[0] == suma_restante

def main():
    # Solicitar al usuario ingresar los números para formar la lista
    numeros_input = input("Ingrese los números separados por espacios: ")
    lista_numeros = [int(num) for num in numeros_input.split()]
    
    # Imprimir la lista original
    print("Lista original:", lista_numeros)
    
    # Realizar la magia numérica
    resultado = magia_numerica(lista_numeros)
    
    # Imprimir la lista final después de aplicar la magia numérica
    print("Lista final después de la magia numérica:", resultado)
    
    # Verificar si se cumple la condición de magia numérica
    if verificar_magia(resultado):
        print("¡La magia numérica funciona correctamente!")
    else:
        print("Error: La magia numérica no funciona correctamente.")

if __name__ == "__main__":
    main()

