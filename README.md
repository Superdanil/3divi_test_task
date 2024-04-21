3divi-test-task
Тестовое задание Backend Developer Python

Описанный ниже старт программы испытан на Windows 10 и версии python 3.12.
На других ОС запуск не тестировался.

Старт

1. git clone https://github.com/Superdanil/3divi_test_task
2. python3 -m venv venv
3. source venv/bin/activate (см. ОС)
4. Файл example.env переименовать в .env
   
Запуск сервера:

docker-compose up -d --build

Запуск клиента:

В файле .env изменяем CONNECTION_COUNT, CONNECTION_VALUE И DELAY_RANGE на желаемые
Запустить файл client/main.py

I. Лог-файл клиента log.txt сохраняется в директории client. Переписывается при каждом запуске клиента.
II. txt1 и txt2 сохраняются в папке Logs. Не переписываются при каждом запуске клиента.



![Image alt](https://github.com/Superdanil/3divi_test_task/blob/master/UML.jpg)
