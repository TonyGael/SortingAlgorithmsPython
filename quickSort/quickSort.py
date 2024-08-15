def quick_sort(arr):
    array_length = len(arr)
    
    if array_length <= 1:
        return arr
    else:
        # elegimo el último elemento como pivote
        pivot = arr[-1]
        left = []
        right = []
        
        # Particionar la lista en izquierda (menor que pivote) y derecha (mayor que pivote)
        for i in range(array_length-1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        
        # Ahora ordenamos recursivamente las lista y fusionamos con el pivot
        return quick_sort(left) + [pivot] + quick_sort(right)

# Ejecutamos el codigo en __main__
if __name__ == '__main__':
    import random, time
    
    # Genero una lista de 20 números aleatrios
    random_list = [random.randint(1, 100) for _ in range(20)]
    print(f'Lista Original: {random_list}')
    
    # Llamamos a la funcion quick_sort() midiendo el tiempo de ejecución de la misma
    start_time = time.time()
    ordered_list = quick_sort(random_list)
    end_time = time.time()
    
    # presentamos la lista ordenada y su tiempo de ejecución
    print()
    print(f'Lista Ordenada: {ordered_list}')
    print(f'Tiempo de ejecución: {end_time-start_time:.6f} segundos.')