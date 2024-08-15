def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # lista de salida
    count = [0] * 10  # lista de conteo para dígitos 0-9

    # Almacenar el conteo de ocurrencias en count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Cambiar count[i] para que contenga la posición real de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir la lista de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copiar la lista de salida a arr[], para que arr[] contenga los números ordenados
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar el número máximo para saber el número de dígitos
    max_num = max(arr)

    # Hacer counting sort para cada dígito (exp será 1, 10, 100, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Ejemplo de uso
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:")
    print(arr)

    radix_sort(arr)

    print("Lista ordenada con Radix Sort:")
    print(arr)
