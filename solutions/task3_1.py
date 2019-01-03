if __name__ == '__main__':
    arr = input('Введите числа, разделённые пробелом: ').split()
    for x in range(0, len(arr)):
        if((x % 2) == 0):
            print(arr[x])