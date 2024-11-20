def mezcla_directa(F, N):
    """
    Implementa el algoritmo de mezcla directa mostrando cada paso.
    F: Lista principal con los elementos a ordenar.
    N: Número de elementos en F.
    """
    PART = 1 
    paso = 1  

    while PART < ((N + 1) // 2):  # Mientras PART sea menor a la mitad redondeada hacia arriba de N
        print(f"\nPaso {paso}: Tamaño de PART = {PART}")
        print(f"Archivo antes de particionar: {F}")
        # Dividir el archivo en dos particiones F1 y F2
        F1, F2 = particiona(F, PART)
        print(f"Partición F1: {F1}")
        print(f"Partición F2: {F2}")
        # Fusionar las particiones F1 y F2 de forma ordenada
        F = fusiona(F1, F2, PART)
        print(f"Archivo después de fusionar: {F}")
        # Multiplicar PART por 2
        PART *= 2
        paso += 1
    return F


def particiona(F, PART):
    """
    Divide el archivo F en dos listas auxiliares F1 y F2 según el tamaño de PART.
    """
    F1 = []
    F2 = [] 
    
    for i in range(0, len(F), 2 * PART):  # Iterar de 2 * PART en 2 * PART
        F1.extend(F[i:i + PART])         # Primera mitad (hasta PART elementos)
        F2.extend(F[i + PART:i + 2 * PART])  # Segunda mitad (de PART a 2 * PART)
    return F1, F2

def fusiona(F1, F2, PART):
    """
    Fusiona dos listas F1 y F2 en una sola lista ordenada.
    """
    resultado = []  # Lista para almacenar el resultado final
    i = 0 
    j = 0 
    # Mientras haya elementos en ambas particiones
    while i < len(F1) and j < len(F2):
        if F1[i] <= F2[j]: 
            resultado.append(F1[i])
            i += 1
        else:
            resultado.append(F2[j]) 
            j += 1
    resultado.extend(F1[i:])
    resultado.extend(F2[j:])
    return resultado

F = list(map(int, input("Ingresa los elementos del archivo (separados por espacio): ").split()))
N = len(F)

print("\nArchivo inicial:", F)
resultado = mezcla_directa(F, N)

print("\nArchivo ordenado:", resultado)
