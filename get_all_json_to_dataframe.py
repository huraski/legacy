def get_all_json_to_dataframe(directory: str = '.'):
    import os                # импорт модуля os для работы с путями файлов
    import glob              # импорт модуля glob для поиска файлов по маске
    import json              # импорт модуля json для парсинга JSON-файлов
    import pandas as pd      # импорт pandas, библиотеки для обработки табличных данных

    # Определяем шаблон поиска всех файлов с расширением .json в указанной директории
    file_pattern = os.path.join(directory, '*.json')  # объединение пути и шаблона файла
    # Получаем список файлов, соответствующих шаблону
    file_list = glob.glob(file_pattern)                 # glob возвращает список путей к файлам
    # Создаём пустой список для хранения DataFrame, загруженных из файлов
    data_frames = []

    # Перебираем каждый найденный JSON файл
    for filename in file_list:
        # Открываем файл в текстовом режиме с кодировкой UTF-8
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Загружаем JSON-данные в словарь или список Python

        # Преобразуем возможный вложенный JSON в плоскую таблицу DataFrame
        df = pd.json_normalize(data)  # разбивает вложенные структуры в столбцы

        # Добавляем новый столбец с именем исходного файла для отслеживания источника данных
        df['source_file'] = os.path.basename(filename)  # os.path.basename возвращает имя файла из пути
        # Добавляем полученный DataFrame в список
        data_frames.append(df)

    # Объединяем все DataFrame из списка в один, индексируем построчно с пересчётом
    combined_df = pd.concat(data_frames, ignore_index=True)  # соединение таблиц вертикально

    # Возвращаем объединённый DataFrame с данными из всех JSON файлов
    return combined_df


# Блок запускается только при выполнении файла напрямую
if __name__ == '__main__':
    # Вызов функции загрузки всех JSON и создание итогового DataFrame
    df = get_all_json_to_dataframe()
    # Выводим первые 100 строк DataFrame на экран
    print(df.head(100))
    # Выводим общее количество строк (записей) в DataFrame
    print(f'Всего записей: {len(df)}')
