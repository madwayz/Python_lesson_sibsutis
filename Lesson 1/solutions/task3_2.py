if __name__ == '__main__':
    count = 0
    arr = list(input('Введите числа разделяя пробелом: ').split())
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1

    print(count)
