# Общее
Проект содержит [автотест](https://github.com/alderven/mango/blob/master/test_Mango.py) и [Allure отчет](https://rawgit.com/alderven/mango/master/allure-report/index.html) о его прогоне.

# Шаги тест кейса
Шаги тест кейса можно найти [здесь](https://rawgit.com/alderven/mango/master/allure-report/index.html#suites/98d3104e051c652961429bf95fa0b5d6/f553573b0761ee45/) или в таблице ниже:

№  | Шаг | Результат прогона
-- | ------------------- | ---------------------- 
1  | Переходим на страницу выбора номера нашего интернет-магазина | [Прошло](https://rawgit.com/alderven/mango/master/allure-report/index.html#suites/98d3104e051c652961429bf95fa0b5d6/f553573b0761ee45/)
2  | Добавляем больше 1-го номера с помощью кнопки "Выбрать случайный" | [Прошло](https://rawgit.com/alderven/mango/master/allure-report/index.html#suites/98d3104e051c652961429bf95fa0b5d6/f553573b0761ee45/)
3  | Проверяем, что номера отображаются в боковой корзине – блок "Текущий заказ" | [Прошло](https://rawgit.com/alderven/mango/master/allure-report/index.html#suites/98d3104e051c652961429bf95fa0b5d6/f553573b0761ee45/)
4  | Проверяем, что Разовый платеж (Подключение), Ежемесячно (Абонентская плата) в блоке "Текущий заказ" соответствуют сумме стоимостей номеров | [Прошло](https://rawgit.com/alderven/mango/master/allure-report/index.html#suites/98d3104e051c652961429bf95fa0b5d6/f553573b0761ee45/)

# Инсталляция
1. Скачать и распаковать архив с проектом: https://github.com/alderven/mango/archive/master.zip
1. Установить Python 3.6 (и выше): https://www.python.org/downloads/
1. Установить следующие библиотики для Python:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * selenium: http://selenium-python.readthedocs.io/installation.html
   * allure-pytest: https://github.com/allure-framework/allure-pytest
   * configparser: https://pypi.python.org/pypi/configparser
1. Установить Allure Framework: https://docs.qameta.io/allure/latest/

# Как запускать тест:
В командной строке выполнить следующую команду:
```javascript
python -m pytest --alluredir full_path_to_report_folder
```
# Как генерировать Allure отчет:
В командной строке выполнить следующую команду:
```javascript
allure serve full_path_to_report_folder
```
