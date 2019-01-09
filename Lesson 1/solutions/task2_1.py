import sys

if __name__ == "__main__":
    answer = 1
    n = int(input('Введите n!\nОтвет: '))
    if n >= 1:
        for x in range(2, n+1):
            answer *= x
    else:
        print('n должен быть не менее 1')
        sys.exit(0)

    print('n! = ' + str(answer))
