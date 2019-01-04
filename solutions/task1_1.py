import sys


if __name__ == "__main__":
    arr = list(map(int, input('Введите число: ').split()))
    if len(arr) > 4:
        print('Слишком много чисел')
        sys.exit(0)

    for element in arr:
        if element < 1 or element > 8:
            print('Числа должны быть в диапазоне от 1 до 8')
            sys.exit(0)

    print(sum(arr) % 2 == 0)
