import sys

if __name__ == "__main__":
    answ = 1
    n = int(input('Введите n!\nОтвет: '))
    if n >= 1:
        for x in range(2, n+1):
            answ *= x
    else:
        print('n должен быть не менее 1')
        sys.exit(0)
    print('n! = ' + str(answ))
