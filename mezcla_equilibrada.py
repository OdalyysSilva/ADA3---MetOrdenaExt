def find_natural_runs(data):
    """
    Encuentra las subsecuencias ordenadas (runs) naturales en la lista.
    """
    runs = []
    current_run = [data[0]]  # Comenzamos con el primer elemento
    
    for i in range(1, len(data)):
        if data[i] >= data[i - 1]:  # Verificar si el siguiente elemento sigue el orden
            current_run.append(data[i])
        else:
            runs.append(current_run)  # Guardar la sublista actual
            current_run = [data[i]]  # Iniciar una nueva sublista
    runs.append(current_run)  # Agregar la última sublista
    
    return runs

def merge_lists(list1, list2):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.
    """
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Agregar los elementos restantes
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

def natural_merge_sort(data):
    """
    Ordena una lista usando el método de mezcla natural.
    """
    print(f"Lista inicial: {data}")
    runs = find_natural_runs(data)
    print(f"Runs iniciales: {runs}")
    
    # Mezclar iterativamente las runs hasta que quede una sola lista
    iteration = 1
    while len(runs) > 1:
        print(f"\n--- Iteración {iteration} ---")
        merged_runs = []
        
        # Mezclar las runs en pares
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):  # Si hay dos runs para mezclar
                merged = merge_lists(runs[i], runs[i + 1])
                print(f"Mezclando {runs[i]} y {runs[i + 1]} -> {merged}")
                merged_runs.append(merged)
            else:  # Si queda una run sin pareja
                merged_runs.append(runs[i])
        
        runs = merged_runs
        iteration += 1
        print(f"Runs después de la iteración: {runs}")
    
    return runs[0]

# Datos de prueba
data = [9,75,14,68,29,17,31,25,4,5,13,18,72,46,61]
sorted_data = natural_merge_sort(data)
print("\nLista ordenada final:", sorted_data)
