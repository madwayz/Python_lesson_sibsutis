def factorial(n):
    answer = 1
    if n >= 1:
        for x in range(2, n+1):
            answer *= x
        print('n! = ', str(answer))
    else:
        print('n должен быть не менее 1')


if __name__ == "__main__":
    factorial(int(input('Введите n!\nОтвет: ')))
