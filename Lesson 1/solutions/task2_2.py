def get_fib_num(a):
    if a < 2:
        return a

    n = 2  #  Счётчик
    previous_num = 1
    current_num = 1
    while current_num < a:
        current_num, previous_num = current_num + previous_num, current_num
        n += 1
    return n if a == current_num else False


if __name__ == '__main__':
    print(str(get_fib_num(int(input('Input n: ')))))
