import requests
from bs4 import BeautifulSoup as BS
import time


CITIES = {
    'Астана': 'astana',
    'Алматы': 'almaty',
    'Шымкент': 'shymkent',
}

shymkent_districts = ['Абайский р-н', 'Аль-Фарабийский р-н', 'Енбекшинский р-н', 'Каратауский р-н', 'Туранский р-н']

astana_districts = ['Алматинский р-н', 'Байконурский р-н', 'Есильский р-н', 'Нуринский р-н', 'Сарыаркинский р-н']

almaty_districts = ['Алатауский р-н', 'Алмалинский р-н', 'Ауэзовский р-н', 'Бостандыкский р-н', 'Жетысуский р-н',
                    'Медеуский р-н', 'Наурызбайский р-н', 'Турксибский р-н']


def open_buy_krisha_almaty():
    info_for_sell_build_almaty = []

    for i in range(1, 500):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/58.0.3029.110 Safari/537.3"}
        r = requests.get('https://krisha.kz/prodazha/kvartiry/' + f'{CITIES["Алматы"]}' + '/?page=' + f'{i}', headers)

        html = BS(r.content, 'html.parser')
        for el in html.select('.a-card__inc .a-card__descr'):
            title = el.select_one('.a-card__header-left a')
            price = el.select_one('.a-card__price')
            address = el.select_one('.a-card__subtitle')
            complex_label = ''
            complex_info = el.find_next('div', class_='a-card__owner a-card__complex-info')

            if complex_info:
                complex_label = complex_info.select_one('.a-card__complex-label').text.strip()

            header = title.text.strip().split(', ')
            if len(header) == 2:
                header.append('')

            address = address.text.strip().split(', ')
            loc_address = ''
            for j in range(1, len(address)):
                loc_address += address[j]

            region = address[0] if address[0] in almaty_districts else None
            if region:
                info = {
                    "room": int(str(header[0][0]).strip()) if header[0] else "N/A",
                    "area": float(str(header[1]).strip().replace('м²', '')) if header[1] else "N/A",
                    "price": int(
                        price.text.replace('〒', '').replace('\xa0', '').replace('от', '').strip()) if price else "N/A",
                    "region": region,
                    "complex_Label": complex_label if complex_label else "N/A",
                }

                info_for_sell_build_almaty.append(info)

        if i % 15 == 0:
            time.sleep(30)

    return info_for_sell_build_almaty


def open_buy_krisha_astana():
    info_for_sell_build_astana = []

    for i in range(1, 500):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/58.0.3029.110 Safari/537.3"}
        r = requests.get('https://krisha.kz/prodazha/kvartiry/' + f'{CITIES["Астана"]}' + '/?page=' + f'{i}', headers)

        html = BS(r.content, 'html.parser')
        for el in html.select('.a-card__inc .a-card__descr'):
            title = el.select_one('.a-card__header-left a')
            price = el.select_one('.a-card__price')
            address = el.select_one('.a-card__subtitle')
            complex_label = ''
            complex_info = el.find_next('div', class_='a-card__owner a-card__complex-info')

            if complex_info:
                complex_label = complex_info.select_one('.a-card__complex-label').text.strip()

            header = title.text.strip().split(', ')
            if len(header) == 2:
                header.append('')

            address = address.text.strip().split(', ')
            loc_address = ''
            for j in range(1, len(address)):
                loc_address += address[j]
            region = address[0] if address[0] in astana_districts else None
            if region:
                info = {
                    "room": int(str(header[0][0]).strip()) if header[0] else "N/A",
                    "area": float(str(header[1]).strip().replace('м²', '')) if header[1] else "N/A",
                    "price": int(
                        price.text.replace('〒', '').replace('\xa0', '').replace('от', '').strip()) if price else "N/A",
                    "region": region,
                    "complex_Label": complex_label if complex_label else "N/A",
                }

                info_for_sell_build_astana.append(info)

        if i % 15 == 0:
            time.sleep(30)

    return info_for_sell_build_astana


def open_buy_krisha_shymkent():
    info_for_sell_build_shymkent = []

    for i in range(1, 400):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/58.0.3029.110 Safari/537.3"}
        r = requests.get('https://krisha.kz/prodazha/kvartiry/' + f'{CITIES["Шымкент"]}' + '/?page=' + f'{i}', headers)

        html = BS(r.content, 'html.parser')
        for el in html.select('.a-card__inc .a-card__descr'):
            title = el.select_one('.a-card__header-left a')
            price = el.select_one('.a-card__price')
            address = el.select_one('.a-card__subtitle')
            complex_label = ''
            complex_info = el.find_next('div', class_='a-card__owner a-card__complex-info')

            if complex_info:
                complex_label = complex_info.select_one('.a-card__complex-label').text.strip()

            header = title.text.strip().split(', ')
            if len(header) == 2:
                header.append('')

            address = address.text.strip().split(', ')
            loc_address = ''
            for j in range(1, len(address)):
                loc_address += address[j]
            region = address[0] if address[0] in shymkent_districts else None
            if region:
                info = {
                    "room": int(str(header[0][0]).strip()) if header[0] else "N/A",
                    "area": float(str(header[1]).strip().replace('м²', '')) if header[1] else "N/A",
                    "price": int(
                        price.text.replace('〒', '').replace('\xa0', '').replace('от', '').strip()) if price else "N/A",
                    "region": region,
                    "complex_Label": complex_label if complex_label else "N/A",
                }

                info_for_sell_build_shymkent.append(info)

        if i % 15 == 0:
            time.sleep(30)

    return info_for_sell_build_shymkent
