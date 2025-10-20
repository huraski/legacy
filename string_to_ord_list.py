def string_to_ord_list(text: str) -> list:
    """
    Преобразует строку в список числовых кодов символов с помощью ord().
    Каждый символ строки преобразуется в свой Unicode код (int).
    Возвращаемый результат — list of int, то есть список целых чисел.
    """
    result = [ord(char) for char in str(text)]  # list comprehension для преобразования
    return result


if __name__ == '__main__':
    sample_text = "Hello World! :)"
    codes = string_to_ord_list(sample_text)
    print(codes)  # Вывод: [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33, 32, 58, 41]

