if __name__ == '__main__':
    n, m, k = map(int, input('Input n, m, k: ').split())
    print(n * m > k and k % n == 0 or k % m == 0)
