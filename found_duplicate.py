def found_duplicate(string: str) -> list:
    """Функция ищет повторяющиеся буквы"""
    string = string.lower()
    letters_set = set(string)
    duplicate = [x for x in letters_set if string.count(x) >= 2]
    return duplicate


print(*found_duplicate(input('Введите слово ')))
