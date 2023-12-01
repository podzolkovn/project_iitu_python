import pandas
from write_to_csv import check_file_buy_shymkent, check_file_buy_astana, check_file_buy_almaty
from math import ceil


PRICE_PER_YEAR = {
    'Астана': {
        2015: {'price_per_area_metr': 335000},
        2016: {'price_per_area_metr': 369000},
        2017: {'price_per_area_metr': 391000},
        2018: {'price_per_area_metr': 409000},
        2019: {'price_per_area_metr': 433000},
        2020: {'price_per_area_metr': 453000},
        2021: {'price_per_area_metr': 479000},
        2022: {'price_per_area_metr': 517000}
    },
    'Алматы': {
        2015: {'price_per_area_metr': 257000},
        2016: {'price_per_area_metr': 283000},
        2017: {'price_per_area_metr': 300000},
        2018: {'price_per_area_metr': 312000},
        2019: {'price_per_area_metr': 329000},
        2020: {'price_per_area_metr': 344000},
        2021: {'price_per_area_metr': 361000},
        2022: {'price_per_area_metr': 396000}
    },
    'Шымкент': {
        2015: {'price_per_area_metr': 364000},
        2016: {'price_per_area_metr': 398000},
        2017: {'price_per_area_metr': 420000},
        2018: {'price_per_area_metr': 438000},
        2019: {'price_per_area_metr': 462000},
        2020: {'price_per_area_metr': 483000},
        2021: {'price_per_area_metr': 509000},
        2022: {'price_per_area_metr': 547000}
    }
}


def prediction_almaty():
    check_file_buy_almaty()
    read_file = pandas.read_csv('date/buy_build_almaty.csv')
    avg_price_per_area_metr = ceil(read_file['price_per_area_metr'].mean())

    add_new = {2023: {
        'price_per_area_metr': avg_price_per_area_metr
    }}

    PRICE_PER_YEAR.get('Алматы').update(add_new)

    mid_list = []
    for key, value in PRICE_PER_YEAR.get('Алматы').items():
        for val in value.values():
            middle = {
                'date': key,
                'price': val
            }
            mid_list.append(middle)
    data_frame = pandas.DataFrame({
        'date': [year.get('date') for year in mid_list],
        'price': [price.get('price') for price in mid_list]
    })
    data_frame.to_csv('date/prediction_almaty.csv')


def prediction_astana():
    check_file_buy_astana()
    read_file = pandas.read_csv('date/buy_build_astana.csv')
    avg_price_per_area_metr = ceil(read_file['price_per_area_metr'].mean())

    add_new = {2023: {
        'price_per_area_metr': avg_price_per_area_metr
    }}

    PRICE_PER_YEAR.get('Астана').update(add_new)

    mid_list = []
    for key, value in PRICE_PER_YEAR.get('Астана').items():
        for val in value.values():
            middle = {
                'date': key,
                'price': val
            }
            mid_list.append(middle)
    data_frame = pandas.DataFrame({
        'date': [year.get('date') for year in mid_list],
        'price': [price.get('price') for price in mid_list]
    })
    data_frame.to_csv('date/prediction_astana.csv')


def prediction_shymkent():
    check_file_buy_shymkent()
    read_file = pandas.read_csv('date/buy_build_shymkent.csv')
    avg_price_per_area_metr = ceil(read_file['price_per_area_metr'].mean())

    add_new = {2023: {
        'price_per_area_metr': avg_price_per_area_metr
    }}

    PRICE_PER_YEAR.get('Шымкент').update(add_new)

    mid_list = []
    for key, value in PRICE_PER_YEAR.get('Шымкент').items():
        for val in value.values():
            middle = {
                'date': key,
                'price': val
            }
            mid_list.append(middle)
    data_frame = pandas.DataFrame({
        'date': [year.get('date') for year in mid_list],
        'price': [price.get('price') for price in mid_list]
    })
    data_frame.to_csv('date/prediction_shymkent.csv')
