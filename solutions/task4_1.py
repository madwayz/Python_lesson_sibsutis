if __name__ == '__main__':
    dic = {}
    text = 'one two one tho three'
    for key in text.split():
        dic[key] = dic.get(key, 0) + 1
    print(dic)