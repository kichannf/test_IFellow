class BaseConverter():

    @staticmethod
    def convert(celsius, par):
        if par == 1:
            return celsius + 273
        elif par == 2:
            return 1.8 * celsius + 32
        else:
            return print(
                'Упс, пока что я перевожу только в Кельвины и Фаренгейты'
            )


degrees = int(input('Введите градусы по Цельсию '))
measurement = int(
    input('Для конвертации в Кельвины введите: 1, '
          'для конвертации в Фаренгейты: 2 ')
)
print(BaseConverter.convert(degrees, measurement))
