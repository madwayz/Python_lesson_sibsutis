if __name__ == "__main__":
    arr = list(map(int, input('Введите число: ').split()))
    print(sum(arr) % 2 == 0)
