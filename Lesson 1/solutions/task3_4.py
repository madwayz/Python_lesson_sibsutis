if __name__ == '__main__':
    arr = list(input('Введите числа разделяя пробелом: ').split())
    if (len(arr) % 2) != 0:
        for i in range(0, len(arr)-2, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    else:
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)
