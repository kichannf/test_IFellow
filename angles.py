def watchs_angles(hour: int, minutes: int) -> int:
    """Возвращает угол между часовой и минутной стрелками"""

    if 0 < hour >= 24 or type(hour) is not int:
        raise ValueError("Недопустимый формат времени")
    if 0 < minutes >= 60 or type(hour) is not int:
        raise ValueError("Недопустимый формат времени")
    hour_angels = hour % 12 * 30
    minutes_angels = minutes * 6
    if minutes_angels < hour_angels:
        print(
            f'Угол на часах {hour}:{minutes} '
            f'равен {360 - hour_angels + minutes_angels}'
        )
    else:
        print(
            f'Угол на часах {hour}:{minutes}'
            f' равен {minutes_angels - hour_angels}'
        )


hour = int(input('Введите час от 0 до 24 '))
minutes = int(input('Введите минуты от 0 до 60 '))
print('Запуск программы подсчета угла')
watchs_angles(hour, minutes)
