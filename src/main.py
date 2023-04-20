from src.utils import create_data
from config.config import config_obj
from src.utils import format_date, hide_number_card


def last_operations(file_json: str):
    operations = sorted(create_data(file_json), key=lambda x: x['date'], reverse=True)[0:5]

    for operation in operations:

        date = format_date(operation["date"])
        info_card_to = hide_number_card(operation['to'])
        try:
            info_card_from = hide_number_card(operation['from'])

        except KeyError:
            info_card_from = 'Открыт новый вклад'

        print(f'{date} {operation["description"]}\n'
              f'{info_card_from} -> {info_card_to}\n'
              f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')


if __name__ == '__main__':
    last_operations(config_obj.file_json)
