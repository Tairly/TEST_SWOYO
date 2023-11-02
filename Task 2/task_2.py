def text_stat(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        return {'error': 'Файл не найден'}

    data = data.lower() # Понижение регистра

    paragraphs = data.split('\n\n') # Деление на абзацы
    words = data.split() # Деление на слова

    latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cyrillic_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    unique_char_dict = {}

    # Подсчет уникальных букв в каждом слове для последуещего вычисления их процентного содержания
    for word in words:
        unique_chars = []
        for char in word:
            if (char in latin_alphabet or char in cyrillic_alphabet) and char not in unique_chars :
                unique_chars.append(char)
        for unique_char in unique_chars:
            if unique_char in unique_char_dict:
                unique_char_dict[unique_char] += 1
            else:
                unique_char_dict[unique_char] = 1

    # Заполнение массива буквами с их информацией
    char_f = []
    for char, count in unique_char_dict.items():
        char_count = data.count(char) # Счетчик кол-ва букв проходит по всему тексту,а не по уникальным буквам
        char_percentage = round((count / len(words)) * 100, 1)
        char_f.append({f'{char}': f'{char_count} шт. {char_percentage} %'})

    # Счетчик слов с буквами обоих алфавитов
    bilingual_words = 0
    for word in words:
        if any(char in word for char in cyrillic_alphabet) and any(char in word for char in latin_alphabet):
            bilingual_words += 1

    # Заполенение итогового словаря
    stat_dict = {}

    for dict in char_f:
        stat_dict.update(dict)

    add = {
        'word_amount': len(words),
        'paragraph_amount': len(paragraphs),
        'bilingual_word_amount': bilingual_words
    }

    stat_dict.update(add)
    return stat_dict

# Реализация
filename = 'zadanie.txt'
result = text_stat(filename)
print(result)