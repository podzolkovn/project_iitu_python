from analysis import prediction_almaty, prediction_astana, prediction_shymkent
from mashine_learning import predictions_line_regression


def application():
    while True:
        print(f'{"-" * 35}')
        command = input('Что вы хотите сделать ?\n'
                        '1. Собрать данные с города\n'
                        '2. Сделать предикт цен до 2030 года\n'
                        '3. Выйти\n'
                        'Введите цифру: ').lower()
        print(f'{"-" * 35}')
        match command:
            case '1':
                prediction_almaty()
                prediction_astana()
                prediction_shymkent()
            case '2':
                print('Зависимость от средней цены за квадратный метр и год\n'.title())
                print(predictions_line_regression())
            case '3':
                exit()
            case _:
                continue


application()
