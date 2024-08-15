def heapify(arr, n, i):
    largest = i  # Inicializar el nodo más grande como raíz
    left = 2 * i + 1  # hijo izquierdo = 2*i + 1
    right = 2 * i + 2  # hijo derecho = 2*i + 2

    # Si el hijo izquierdo existe y es mayor que la raíz
    if left < n and arr[i] < arr[left]:
        largest = left

    # Si el hijo derecho existe y es mayor que el nodo más grande hasta ahora
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Si el nodo más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # intercambiar

        # Heapify la raíz afectada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # intercambiar
        heapify(arr, i, 0)

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    import random
    import time

    # Generar una lista de 10 números aleatorios
    random_list = [random.randint(1, 100) for _ in range(10)]
    print("Lista original:", random_list)

    # Medir el tiempo de ejecución
    start_time = time.time()
    sorted_list = heap_sort(random_list)
    end_time = time.time()

    print(f"Lista ordenada: {sorted_list}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
