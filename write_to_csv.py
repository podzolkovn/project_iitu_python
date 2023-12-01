import pandas
from open_site import open_buy_krisha_almaty, open_buy_krisha_astana, open_buy_krisha_shymkent
from math import ceil


def write_in_file_buy_almaty():
    info_buy = open_buy_krisha_almaty()
    data_frame = pandas.DataFrame({
        'id': [i + 1 for i, info in enumerate(info_buy)],
        "room": [info['room'] for info in info_buy],
        "area": [info['area'] for info in info_buy],
        "price": [info['price'] for info in info_buy],
        'price_per_area_metr': [int(ceil(info['price'] / info['area'])) for info in info_buy],
        "region": [info['region'] for info in info_buy],
        "complex_Label": [info['complex_Label'] for info in info_buy],
    })
    data_frame.to_csv('date/buy_build_almaty.csv')


def check_file_buy_almaty():
    try:
        file_read = pandas.read_csv('date/buy_build_almaty.csv')
        print('Файлы уже получены город Алматы')
        return file_read
    except FileNotFoundError:
        write_in_file_buy_almaty()
        check_file_buy_almaty()


def write_in_file_buy_astana():
    info_buy = open_buy_krisha_astana()
    data_frame = pandas.DataFrame({
        'id': [i + 1 for i, info in enumerate(info_buy)],
        "room": [info['room'] for info in info_buy],
        "area": [info['area'] for info in info_buy],
        "price": [info['price'] for info in info_buy],
        'price_per_area_metr': [int(ceil(info['price'] / info['area'])) for info in info_buy],
        "region": [info['region'] for info in info_buy],
        "complex_Label": [info['complex_Label'] for info in info_buy],
    })
    data_frame.to_csv('date/buy_build_astana.csv')


def check_file_buy_astana():
    try:
        file_read = pandas.read_csv('date/buy_build_astana.csv')
        print('Файлы уже получены город Астана')
        return file_read
    except FileNotFoundError:
        write_in_file_buy_astana()
        check_file_buy_astana()


def write_in_file_buy_shymkent():
    info_buy = open_buy_krisha_shymkent()
    data_frame = pandas.DataFrame({
        'id': [i + 1 for i, info in enumerate(info_buy)],
        "room": [info['room'] for info in info_buy],
        "area": [info['area'] for info in info_buy],
        "price": [info['price'] for info in info_buy],
        'price_per_area_metr': [int(ceil(info['price'] / info['area'])) for info in info_buy],
        "region": [info['region'] for info in info_buy],
        "complex_Label": [info['complex_Label'] for info in info_buy],
    })
    data_frame.to_csv('date/buy_build_shimkent.csv')


def check_file_buy_shymkent():
    try:
        file_read = pandas.read_csv('date/buy_build_shymkent.csv')
        print('Файлы уже получены город Шымкент')
        return file_read
    except FileNotFoundError:
        write_in_file_buy_shymkent()
        check_file_buy_shymkent()
