def test_1_id_type_date_to_ord():
    # Тест времени выполнения
    import time
    start_time = time.time()
    
    # Импортируем загрузку json и функцию преобразования строки в список ord
    from get_all_json_to_dataframe import get_all_json_to_dataframe
    from string_to_ord_list import string_to_ord_list

    # Загружаем DataFrame из json файлов, считаем объём памяти им занимаемой
    df = get_all_json_to_dataframe()
    memory_df = df.memory_usage(deep=True).sum()
    print(f"Память до обработки: {memory_df / 1024**2 : .2f} МБ")

    # Применяем функции к столбцам для создания новых
    df['id_ord'] = df['id'].apply(string_to_ord_list)
    df['type_ord'] = df['type'].apply(string_to_ord_list)
    df['date_ord'] = df['date'].apply(string_to_ord_list)

    # Выводим итоговый DataFrame
    print(df)
    memory_df = df.memory_usage(deep=True).sum()
    print(f"Память после обработки: {memory_df / 1024**2 : .2f} МБ")
    print(f"Общее время выполнения: {time.time() - start_time : .2f} секунд")


if __name__ == '__main__':
    test_1_id_type_date_to_ord()
