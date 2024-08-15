def merge_sort(arr):
    n = len(arr)
    if n > 1:
        # punto medio
        mid = n // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # ordenamos cada mitad
        merge_sort(left_half)
        merge_sort(right_half)
        
        # inicializamos el índie para la fusión
        i = j = k = 0
        
        # fucionamos las dos mitades en arr[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j+=1
            k+=1
        
        # Copia los elementos restantes de left_half[], si los hay
        while i < len(left_half):
            arr[k] = left_half[i]
            i+=1
            k+=1
        
        # Copia los elementos restantes de right_half[], si los hay
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr

if __name__ == '__main__':
    
    import random, time
    
    # generamos lista
    random_list = [random.randint(1,100) for _ in range(10)]
    print(f'Listaoriginal: {random_list}')
    
    # medimos tiempo de ejecución
    start_time = time.time()
    sorted_list = merge_sort(random_list)
    end_time = time.time()
    
    print(f'Lista ordenada: {sorted_list}')
    print(f'Tiempo de ejecución: {end_time-start_time:.6f} segundos')
