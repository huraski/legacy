# Вычисляет геоцентрическую долготу планеты от 0 до 360 градусов (от Овна до Рыб)
# по дате рождения с учётом местного времени (по умолчанию +3).

def get_planet_cords(year: int, month: int, day: int,
                         hour: int, minute: int, second: int,
                         planet_id: int, timezone: int=(+3)):
    # year: Год
    # month: Месяц 
    # day: День
    # hour: Час (по местному времени)
    # minute: Минуты
    # second: Секунды
    
    # planet_id: Идентификатор планеты:
    # 0 – Солнце, 1 – Луна, 2 – Меркурий, 3 – Венера,
    # 4 – Марс, 5 – Юпитер, 6 – Сатурн, 7 – Уран,
    # 8 – Нептун, 9 – Плутон, 10 – Раху, 11 – Восх. узел (True),
    # 12 – Лилит, 13 – (Хз что) , 14 – (Отсутствует), 15 – Хирон
    
    # timezone: Сдвиг часового пояса, по умолчанию (+3)

    import swisseph as swe
    from datetime import datetime, timedelta

    dt_local = datetime(year, month, day, hour, minute, second)
    dt = dt_local - timedelta(hours=timezone)
    swe.set_ephe_path('.')  # Путь к файлам эфемерид

    jd = swe.julday(dt.year, dt.month, dt.day,
                    dt.hour + dt.minute / 60 + dt.second / 3600)

    result, flag = swe.calc_ut(jd, planet_id)

    return result
    # result: Список с шестью элементами (list of float):
    # result[0] – геоцентрическая долгота планеты в градусах от 0 до 360
    # result[1] – широта
    # result[2] – расстояние (радиус-вектор)
    # result[3] – скорость изменения долготы
    # result[4] – скорость изменения широты
    # result[5] – скорость изменения расстояния

# Тестовый запуск
if __name__ == '__main__':
    planet_cords = get_planet_cords(1990, 10, 23, 17, 11, 0, planet_id=0, timezone=3)
    print(f"Долгота: {planet_cords[0] : .4f},")
    print(f"Знак: {planet_cords[0] // 30 + 1 : .0f}-й от Овна до Рыб.")
