def test_1_id_type_date_to_ord():
    # Импортируем загрузку json и функцию преобразования строки в список ord
    from get_all_json_to_dataframe import get_all_json_to_dataframe
    from string_to_ord_list import string_to_ord_list

    # Загружаем DataFrame из json файлов
    df = get_all_json_to_dataframe()

    # Применяем функции к столбцам для создания новых
    df['id_ord'] = df['id'].apply(string_to_ord_list)
    df['type_ord'] = df['type'].apply(string_to_ord_list)
    df['date_ord'] = df['date'].apply(string_to_ord_list)

    # Выводим итоговый DataFrame
    print(df)

if __name__ == '__main__':
    test_1_id_type_date_to_ord()
