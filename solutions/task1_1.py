import sys

if __name__ == "__main__":
    arr = list()
    for i in range(4):
        arr.append(int(input('Введите число: ')))
        print(str(i) + ' ' + str(arr[i]))
        if(arr[i] < 1 or arr[i] > 8):
            print('Числа должны быть в диапазоне от 1 до 8')
            sys.exit(0)

    for x in arr:
        if((arr[0] + arr[1]) % 2 == (arr[2] + arr[3]) % 2):
            print('True')
        else: print('False')
    print(arr)