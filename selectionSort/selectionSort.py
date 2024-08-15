import random, time

# definimos la función selection_sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # el indice del elemento minimo asumido de la parte no ordenada
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # ahora intercambiamos el elemento mínimo con el primer elemento no orndeado obtenido de la comparación
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# creamos una lista de 50 números enteros random
random_list = [random.randint(1,100) for _ in range(50)]

# presentamos la lista original
print(f'Lista original: {random_list}')

# llamamos a la función selection_sort()
# medimos la complejidad temporal
start_time = time.time()
sorted_list = selection_sort(random_list)
end_time = time.time()

print()
print(f'Lista ordenada: {sorted_list}')
print(f'Tiempo de ejecución: {end_time - start_time:.6f} segundos.')