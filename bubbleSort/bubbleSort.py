import random, time

def bubble_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        # creamos una variable llamada swapped  que usaremos para verificar si hubo algún intercambio
        swapped = False
        
        # ahora iteramos hasta el último elemento del array
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # si se cumple la condición el elemento actual es mayor que el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # la lista ya esta ordenada sino hubo intercambios, se devuelve arr
        if not swapped:
            break
    return arr

# creamos una lista de 50 numeros random
random_list = [random.randint(1, 100) for _ in range(50)]

# presentamos la lista original
print(f'Lista original: {random_list}')

# Llamamos a la función bubble_sort()
# Tambien medimos la complejidad temporal
start_time = time.time()
sorted_list = bubble_sort(random_list)
end_time = time.time()

print()
print(f'Lista ordenada: {sorted_list}')
print(f'Tiempo de ejecución: {end_time - start_time:.6f} segundos')
