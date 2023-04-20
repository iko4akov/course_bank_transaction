# Show history transaction

---

## Start code
### Warning

в случае, распаковки архива локально, следует учитывать, что в файле **[operations.json](operations.json)** на `1104` строке
находится пустой словарь `{}`, который необходимо удалить в ручную для корректной работы программы_


`run run.py`

---
## Start tests
`python -m pytest`

## Coverage tests

`pytest --cov .\src\ --cov-report term-missing`

---
## Code Description
The code reads the data from the operations.json file 
(using [unzip_file.py](unzip_file/unzip_file.py) unpacks from the
[operations.zip](operations.zip) archive)*, sorts them by date of
operations and displays information about the last five operations.

*_in case of unpacking the archive locally, please note that in 
the [operations.json](operations.json) file on line `1104` there 
is an empty dictionary `{}`, which must be deleted manually for 
the program to work correctly_

The `create_data` function in `utils.py` reads the JSON file and 
returns a list of dictionaries containing information about each operation. 

The `config.py` file contains configuration settings, including 
the path to the JSON file. 

The `format_date` function in `utils.py` takes a date string in 
ISO format and returns a formatted date string in the format "dd.mm.yyyy".

The `hide_number_card` function in `utils.py` takes a string 
representing a bank account or debit(credit) card number and returns a masked string with only the first and last two digits visible. 

The `last_operations` function in the main code file uses the 
above functions to print the details of the last five operations. It formats the date using `format_date` and masks the 
card numbers using `hide_number_card`. If there is no "from" account specified for an operation, it assumes that a new 
account has been opened. 

The main code block calls the `last_operations` function with the path to the JSON file specified in `config.py`.

Also in the folder [tests](tests) there are tests:

- [test_create_data.py](tests%2Ftest_create_data.py) for testing `create_data`
- [test_formate_date.py](tests%2Ftest_formate_date.py) for testing `format_date`
- [test_hide_number_card.py](tests%2Ftest_hide_number_card.py) for testing `hide_number_card`


### Описание кода (Русская версия)
Код считывает данные из файла **[operations.json](operations.json)** (с помощью [unzip_file.py](unzip_file/unzip_file.py) распаковывается из архива [operations.zip](operations.zip))*, сортирует их по дате операций и выводит сведения о последних 
пяти операциях.

Функция `create_data` в `utils.py` читает файл **JSON** и возвращает список словарей, 
содержащих информацию о каждой операции.

Файл `config.py` содержит параметры конфигурации, включая путь к файлу **JSON**.

Функция `format_date` в `utils.py` принимает строку даты в формате ISO и возвращает отформатированную строку даты 
в формате **«дд.мм.гггг»**.

Функция `hide_number_card` в `utils.py` принимает строку, представляющую номер счета или дебетовой(кредитной) карты,
и возвращает замаскированную строку, в которой видны только первая и две последние цифры.

Функция `last_operations` в основном файле кода использует вышеуказанные функции для вывода сведений о последних пяти операциях.
Она форматирует дату с помощью `format_date` и маскирует номера карт с помощью `hide_number_card`. Если для операции не указан счёт «от», 
предполагается, что было открытие счета.

Так же в папке [tests](tests) имеются тесты:
- [test_create_data.py](tests%2Ftest_create_data.py) для тестирования `create_data`
- [test_formate_date.py](tests%2Ftest_formate_date.py) для тестирования `format_date`
- [test_hide_number_card.py](tests%2Ftest_hide_number_card.py) для тестирования `hide_number_card`

![codewars](https://www.codewars.com/users/Ko4ak/badges/micro)
