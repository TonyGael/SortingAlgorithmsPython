def counting_sort(arr):
    # Encuentra el elemento máximo y mínimo en arr
    max_val = max(arr)
    min_val = min(arr)
    
    # Rango de los valores en arr
    range_of_elements = max_val - min_val + 1

    # Inicializa la lista de conteo
    count = [0] * range_of_elements

    # Almacena el conteo de cada elemento
    for num in arr:
        count[num - min_val] += 1

    # Modifica el conteo para que contenga la posición real de este elemento en la lista de salida
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Inicializa la lista de salida
    output = [0] * len(arr)

    # Construye la lista de salida
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    # Copia la lista de salida en arr para que arr contenga los elementos ordenados
    for i in range(len(arr)):
        arr[i] = output[i]

# Ejemplo de uso
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Lista original:")
    print(arr)

    counting_sort(arr)

    print("Lista ordenada con Counting Sort:")
    print(arr)
