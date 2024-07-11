import allure
import requests
import url
import pytest
import helpers


class TestOrderCreate:
    @allure.title('Выбор цвета при создании заказа')
    @allure.description('Создание нового заказа без заполненного поля "цвет"')
    def test_success_order_without_color(self):
        payload = helpers.generate_order_details()
        response = requests.post(url.URL_BASE + url.URL_ORDER, data=payload)
        assert response.status_code == 201 and 'track' in response.json()

    @allure.description('Создание нового заказа с разными вариантами поля "цвет"')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY', 'BLACK, GREY'])
    def test_success_order_with_any_colors(self, color):
        payload = helpers.generate_order_details()
        payload.setdefault(color, []).append(color)
        response = requests.post(url.URL_BASE + url.URL_ORDER, data=payload)
        assert response.status_code == 201 and 'track' in response.json()

class TestOrderList:
    @allure.title('Тело ответа возвращает список заказов')
    @allure.description('Тело ответа возвращает список заказов')
    def test_success_orders_list(self):
        response = requests.get(url.URL_BASE + url.URL_ORDER)
        assert response.status_code == 200 and response.json()['orders'] != []
