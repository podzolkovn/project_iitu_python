import pandas
from open_site import open_buy_krisha
from math import ceil


def write_in_file_buy():
    info_buy = open_buy_krisha()
    data_frame = pandas.DataFrame({
        'id': [i + 1 for i, info in enumerate(info_buy)],
        "room": [info['room'] for info in info_buy],
        "area": [info['area'] for info in info_buy],
        "price": [info['price'] for info in info_buy],
        'price_per_area_metr': [int(ceil(info['price'] / info['area'])) for info in info_buy],
        "region": [info['region'] for info in info_buy],
        "address": [info['address'] for info in info_buy],
        "description": [info['description'] for info in info_buy],
        "complex_Label": [info['complex_Label'] for info in info_buy],
        "complex_Name": [info['complex_Name'] for info in info_buy],
        "complex_Developer": [info['complex_Developer'] for info in info_buy],
        "year": 2023
    })
    data_frame.to_csv('date/buy_build_aktau.csv')


def check_file_buy():
    try:
        file_read = pandas.read_csv('date/buy_build_aktau.csv')
        return file_read
    except FileNotFoundError:
        write_in_file_buy()
        check_file_buy()
