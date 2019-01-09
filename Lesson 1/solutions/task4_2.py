from collections import defaultdict

if __name__ == '__main__':
    lat_eng = defaultdict(list)
    counter = int(input('Введите кол-во английских слов: '))
    print(
        """
        Заполните словарь.\n
        Пример: apple - malum, pomum, popula\n
        """
        )

    for _ in range(counter):
        eng_word, lat_translate_from_eng = input('Осталось ' + str(counter) + ' | Ответ: ').split(' - ')

        for lat_word in lat_translate_from_eng.split(', '):
            lat_eng[lat_word].append(eng_word)
        counter -= 1

    print(len(lat_eng))
    for lat, eng_translate in sorted(lat_eng.items()):
        print(lat + ' - ' + ', '.join(eng_translate))
