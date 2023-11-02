def roman_numerals_to_int(roman_numeral):
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    # Список неправильных комбинаций цифр
    invalid_combinations = {'IIII','VV','XXXX','LL','CCCC','DD'}

    # Проверка на неверные комбинации
    for combination in invalid_combinations:
        if combination in roman_numeral:
            return None

    # Словарь для перевода римских цифр в арабские
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Обратный цикл для конвертации
    result = 0
    prev1_value = 0
    prev2_value = 0

    for numeral in reversed(roman_numeral):
        # Проверка на неверные символы
        if numeral not in symbols:
            return None

        value = roman_numerals.get(numeral)
        # Проверка на нарушение последовательности
        if (value == prev1_value and value < prev2_value
                or value < prev1_value and value == prev2_value
                or value < prev1_value < prev2_value)\
                or prev1_value < value < prev2_value:
            return None
        elif value < prev1_value:
            result -= value # Значение уменьшается, если число слева меньше числа справа
        else:
            result += value # В противном случае значение увеличивается
        prev2_value = prev1_value
        prev1_value = value # Хранение предыдущих цифр

    return result

# Реализация
roman_numeral = "XLIV"
print(roman_numerals_to_int(roman_numeral))