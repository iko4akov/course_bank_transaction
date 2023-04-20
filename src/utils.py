import json
from datetime import datetime


def create_data(filename: str) -> dict:
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

        return data


def format_date(date: str) -> str:
    date_format: datetime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    date_show: str = datetime.strftime(date_format, "%d.%m.%Y")

    return date_show


def hide_number_card(info_card: str) -> str:
    info_card_list = info_card.split()

    service_card = ""
    num_card = ""
    for index in info_card_list:

        if index.isalpha():
            service_card += index + " "

        elif index.isdigit() and len(index) == 16:
            num_card = index.replace(index[4:12], f" {index[4:6]}** **** ")

        elif index.isdigit() and len(index) == 20:
            num_card = '**' + index[-4:]

    return f'{service_card}{num_card}'
