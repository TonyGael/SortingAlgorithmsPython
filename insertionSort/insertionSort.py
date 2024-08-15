import random, time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Mueve los elementos de arr[0..i-1] que son mayores que key a una posición adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# generamos una lista de 20 números aleatoria
random_list = [random.randint(1,100) for _ in range(20)]

# imprimimos lista original
print(f'Lista original: {random_list}')

# llamamos a la funcion y medimos la complejidad temporal
start_time = time.time()
sorted_list = insertion_sort(random_list)
end_time = time.time()

print()
print(f'Lista ordenada: {sorted_list}')
print(f'Tiempo de ejecución: {end_time - start_time:.6f} segundos.')