def intercalacion(lista1, lista2):
    i, j = 0, 0
    resultado = []
    paso = 1
    while i < len(lista1) and j < len(lista2):
        print(f"Paso {paso}: Comparando {lista1[i]} y {lista2[j]}")
        if lista1[i] < lista2[j]:
            print(f"-> {lista1[i]} es menor. Agregando {lista1[i]} al resultado.")
            resultado.append(lista1[i])
            i += 1
        else:
            print(f"-> {lista2[j]} es menor o igual. Agregando {lista2[j]} al resultado.")
            resultado.append(lista2[j])
            j += 1
        print(f"Resultado actual: {resultado}\n")
        paso += 1

    if i < len(lista1):
        print(f"Paso {paso}: Agregando los elementos restantes de lista1: {lista1[i:]}")
        resultado.extend(lista1[i:])
        print(f"Resultado actual: {resultado}\n")
        paso += 1

    if j < len(lista2):
        print(f"Paso {paso}: Agregando los elementos restantes de lista2: {lista2[j:]}")
        resultado.extend(lista2[j:])
        print(f"Resultado actual: {resultado}\n")

    return resultado

lista1 = [1, 3, 9, 23, 50, 66]
lista2 = [5, 6, 10, 30, 35, 44]
print("Resultado de la intercalación:", intercalacion(lista1, lista2))
