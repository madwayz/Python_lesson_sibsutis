if __name__ == '__main__':
    arr = map(int, input('Input numbers separated by space: ').split())
    result_sum = 0
    result_multiply = 1

    for element in arr:
        result_sum += element
        result_multiply *= element

    print(result_sum,  result_multiply)