def mezcla_equilibrada_ordenar(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    print(f"Dividiendo: {lista} -> Izquierda: {lista[:medio]}, Derecha: {lista[medio:]}")
    
    izquierda = mezcla_equilibrada_ordenar(lista[:medio])
    derecha = mezcla_equilibrada_ordenar(lista[medio:])
    
    resultado = mezclar(izquierda, derecha)
    print(f"Resultado combinado: {resultado}")
    
    return resultado

def mezclar(izquierda, derecha):
    resultado = []
    indice_izquierda, indice_derecha = 0, 0
    
    while indice_izquierda < len(izquierda) and indice_derecha < len(derecha):
        if izquierda[indice_izquierda] < derecha[indice_derecha]:
            resultado.append(izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            resultado.append(derecha[indice_derecha])
            indice_derecha += 1
            
    resultado.extend(izquierda[indice_izquierda:])
    resultado.extend(derecha[indice_derecha:])
    
    print(f"Mezclando: {izquierda} y {derecha} -> {resultado}")
    return resultado

def main():
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)
    print("\nProcesando:\n")
    
    lista_ordenada = mezcla_equilibrada_ordenar(lista)
    print("\nLista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()
