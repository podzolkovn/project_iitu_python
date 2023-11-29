import requests
from bs4 import BeautifulSoup as BS
import time


CITIES = {
    'Астана': 'astana',
    'Алматы': 'almaty',
    'Шымкент': 'shymkent',
    'Атырау': 'atyray',
    'Актау': 'aktau'
}


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
            description = el.select_one('.a-card__text-preview')
            complex_label = ''
            complex_name = ''
            complex_developer = ''
            complex_info = el.find_next('div', class_='a-card__owner a-card__complex-info')

            if complex_info:
                complex_label = complex_info.select_one('.a-card__complex-label').text.strip()
                complex_name = complex_info.find('a').text.strip()
                complex_developer = str(complex_info.contents[-1]).strip()

            header = title.text.strip().split(', ')
            if len(header) == 2:
                header.append('')

            address = address.text.strip().split(', ')
            loc_address = ''
            for j in range(1, len(address)):
                loc_address += address[j]
            info = {
                "room": int(str(header[0][0]).strip()) if header[0] else "N/A",
                "area": float(str(header[1]).strip().replace('м²', '')) if header[1] else "N/A",
                "price": int(price.text.replace('〒', '').replace('\xa0', '').replace('от',
                                                                                     '').strip()) if price else "N/A",
                "region": address[0] if address[0] else "N/A",
                "address": loc_address if loc_address else "N/A",
                "description": description.text.strip() if description else "N/A",
                "complex_Label": complex_label if complex_label else "N/A",
                "complex_Name": complex_name if complex_name else "N/A",
                "complex_Developer": complex_developer if complex_developer else "N/A"
            }

            info_for_sell_build_almaty.append(info)

        if i % 15 == 0:
            time.sleep(30)

    return info_for_sell_build_almaty


def open_buy_krisha_aktau():
    info_for_sell_build_aktau = []

    for i in range(1, 500):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/58.0.3029.110 Safari/537.3"}
        r = requests.get('https://krisha.kz/prodazha/kvartiry/' + f'{CITIES["Актау"]}' + '/?page=' + f'{i}', headers)

        html = BS(r.content, 'html.parser')
        for el in html.select('.a-card__inc .a-card__descr'):
            title = el.select_one('.a-card__header-left a')
            price = el.select_one('.a-card__price')
            address = el.select_one('.a-card__subtitle')
            description = el.select_one('.a-card__text-preview')
            complex_label = ''
            complex_name = ''
            complex_developer = ''
            complex_info = el.find_next('div', class_='a-card__owner a-card__complex-info')

            if complex_info:
                complex_label = complex_info.select_one('.a-card__complex-label').text.strip()
                complex_name = complex_info.find('a').text.strip()
                complex_developer = str(complex_info.contents[-1]).strip()

            header = title.text.strip().split(', ')
            if len(header) == 2:
                header.append('')

            address = address.text.strip().split(', ')
            loc_address = ''
            for j in range(1, len(address)):
                loc_address += address[j]
            info = {
                "room": int(str(header[0][0]).strip()) if header[0] else "N/A",
                "area": float(str(header[1]).strip().replace('м²', '')) if header[1] else "N/A",
                "price": int(price.text.replace('〒', '').replace('\xa0', '').replace('от',
                                                                                     '').strip()) if price else "N/A",
                "region": address[0] if address[0] else "N/A",
                "address": loc_address if loc_address else "N/A",
                "description": description.text.strip() if description else "N/A",
                "complex_Label": complex_label if complex_label else "N/A",
                "complex_Name": complex_name if complex_name else "N/A",
                "complex_Developer": complex_developer if complex_developer else "N/A"
            }

            info_for_sell_build_aktau.append(info)

        if i % 15 == 0:
            time.sleep(30)

    return info_for_sell_build_aktau


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
            description = el.select_one('.a-card__text-preview')
            complex_label = ''
            complex_name = ''
            complex_developer = ''
            complex_info = el.find_next('div', class_='a-card__owner a-card__complex-info')

            if complex_info:
                complex_label = complex_info.select_one('.a-card__complex-label').text.strip()
                complex_name = complex_info.find('a').text.strip()
                complex_developer = str(complex_info.contents[-1]).strip()

            header = title.text.strip().split(', ')
            if len(header) == 2:
                header.append('')

            address = address.text.strip().split(', ')
            loc_address = ''
            for j in range(1, len(address)):
                loc_address += address[j]
            info = {
                "room": int(str(header[0][0]).strip()) if header[0] else "N/A",
                "area": float(str(header[1]).strip().replace('м²', '')) if header[1] else "N/A",
                "price": int(price.text.replace('〒', '').replace('\xa0', '').replace('от',
                                                                                     '').strip()) if price else "N/A",
                "region": address[0] if address[0] else "N/A",
                "address": loc_address if loc_address else "N/A",
                "description": description.text.strip() if description else "N/A",
                "complex_Label": complex_label if complex_label else "N/A",
                "complex_Name": complex_name if complex_name else "N/A",
                "complex_Developer": complex_developer if complex_developer else "N/A"
            }

            info_for_sell_build_astana.append(info)

        if i % 15 == 0:
            time.sleep(30)

    return info_for_sell_build_astana


def open_buy_krisha_shymkent():
    info_for_sell_build_shymkent = []

    for i in range(1, 500):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/58.0.3029.110 Safari/537.3"}
        r = requests.get('https://krisha.kz/prodazha/kvartiry/' + f'{CITIES["Шымкент"]}' + '/?page=' + f'{i}', headers)

        html = BS(r.content, 'html.parser')
        for el in html.select('.a-card__inc .a-card__descr'):
            title = el.select_one('.a-card__header-left a')
            price = el.select_one('.a-card__price')
            address = el.select_one('.a-card__subtitle')
            description = el.select_one('.a-card__text-preview')
            complex_label = ''
            complex_name = ''
            complex_developer = ''
            complex_info = el.find_next('div', class_='a-card__owner a-card__complex-info')

            if complex_info:
                complex_label = complex_info.select_one('.a-card__complex-label').text.strip()
                complex_name = complex_info.find('a').text.strip()
                complex_developer = str(complex_info.contents[-1]).strip()

            header = title.text.strip().split(', ')
            if len(header) == 2:
                header.append('')

            address = address.text.strip().split(', ')
            loc_address = ''
            for j in range(1, len(address)):
                loc_address += address[j]
            info = {
                "room": int(str(header[0][0]).strip()) if header[0] else "N/A",
                "area": float(str(header[1]).strip().replace('м²', '')) if header[1] else "N/A",
                "price": int(price.text.replace('〒', '').replace('\xa0', '').replace('от',
                                                                                     '').strip()) if price else "N/A",
                "region": address[0] if address[0] else "N/A",
                "address": loc_address if loc_address else "N/A",
                "description": description.text.strip() if description else "N/A",
                "complex_Label": complex_label if complex_label else "N/A",
                "complex_Name": complex_name if complex_name else "N/A",
                "complex_Developer": complex_developer if complex_developer else "N/A"
            }

            info_for_sell_build_shymkent.append(info)

        if i % 15 == 0:
            time.sleep(30)

    return info_for_sell_build_shymkent
