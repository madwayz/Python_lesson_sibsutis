if __name__ == '__main__':
    dic = {}
    text = input('Введите текст: ')
    for key in text.split():
        dic[key] = dic.get(key, 0) + 1
    print(dic)