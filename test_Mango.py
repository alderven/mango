import pytest
from random import randint
from page import PageNumbers


@pytest.allure.feature('Интернет-магазин')
@pytest.allure.story('Выбор номера')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_mango(driver):

    with pytest.allure.step('1. Переходим на страницу выбора номера нашего интернет-магазина'):
        page = PageNumbers(driver)
        title = 'Покупка многоканальных номеров Многоканальные номера'
        err_msg = 'Актуальный заголовок страницы: "{}". Ожидаемый заголовок страницы: "{}"'.format(page.driver.title, title)
        assert page.driver.title == title, err_msg

    with pytest.allure.step('2. Добавляем больше 1-го номера с помощью кнопки "Выбрать случайный"'):
        numbers_count = randint(2, 9)
        page.select_random_numbers(numbers_count)

    with pytest.allure.step('3. Проверяем, что номера отображаются в боковой корзине – блок "Текущий заказ"'):

        err_msg = 'Номеров добавлено в корзину: {}. Номеров в корзине: {}'.format(numbers_count, page.cart.numbers_in_cart)
        assert numbers_count == page.cart.numbers_in_cart, err_msg

    with pytest.allure.step('4. Проверяем, что Разовый платеж (Подключение), Ежемесячно (Абонентская плата) в блоке "Текущий заказ" соответствуют сумме стоимостей номеров.'):
        total_price_cart = page.cart.one_time_payment + page.cart.monthly_payment
        total_price_page = (page.connection_price + page.regular_price) * numbers_count
        err_msg = '''Сумма в разделе "Текущий заказ": {} не соответствует сумме стоимостей номеров: {}.
                  'Заказано номеров: {}, разовый платеж: {}, абонентская плата: {}'''.format(
                   total_price_cart, total_price_page, numbers_count, page.connection_price, page.regular_price)
        assert total_price_cart == total_price_page, err_msg
