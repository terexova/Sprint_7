import allure
import requests
import data
import helpers


class TestCourierCreate:
    @allure.title('Создание курьера')
    @allure.description('Успешное создание курьера')
    def test_success_create_courier(self):
        payload = helpers.create_new_courier()
        response = requests.post(data.URL.URL_COURIER, data=payload)
        helpers.delete_courier({'login': payload['login'], 'password': payload['password']})
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.description('Нельзя создать двух одинаковых курьеров')
    def test_fail_create_two_similar_courier(self):
        payload = helpers.create_new_courier()
        requests.post(data.URL.URL_COURIER, data=payload)
        response = requests.post(data.URL.URL_COURIER, data=payload)
        assert (response.status_code == 409 and
                response.json()['message'] == data.TestBodyText.text_courier_409)

    @allure.description('Нельзя создать курьера без обязательного поля login')
    def test_fail_create_courier_without_login(self):
        payload = {'login': '', 'password': '123', 'firstName': 'Olga'}
        response = requests.post(data.URL.URL_COURIER, data=payload)
        assert (response.status_code == 400 and
                response.json()['message'] == data.TestBodyText.text_courier_400)

    @allure.description('Нельзя создать курьера без обязательного поля password')
    def test_fail_create_courier_without_password(self):
        payload = {'login': 'terexova', 'password': '', 'firstName': 'Olga'}
        response = requests.post(data.URL.URL_COURIER, data=payload)
        assert (response.status_code == 400 and
                response.json()['message'] == data.TestBodyText.text_courier_400)

class TestCourierLogin:
    @allure.title('Проверка логина курьера')
    @allure.description('Курьер может авторизоваться')
    def test_success_courier_authorisation(self):
        courier_new = helpers.generate_registration()
        authorisation = {'login': courier_new[0], 'password': courier_new[1]}
        response = requests.post(data.URL.URL_LOGIN, data=authorisation)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.description('Курьер не может авторизоваться без login')
    def test_fail_authorisation_without_login(self):
        courier_new = helpers.generate_registration()
        authorisation = {'login': '', 'password': courier_new[1]}
        response = requests.post(data.URL.URL_LOGIN, data=authorisation)
        assert (response.status_code == 400 and
                response.json()['message'] == 'Недостаточно данных для входа')

    @allure.description('Курьер не может авторизоваться без password')
    def test_fail_authorisation_without_password(self):
        courier_new = helpers.generate_registration()
        authorisation = {'login': courier_new[0], 'password': ''}
        response = requests.post(data.URL.URL_LOGIN, data=authorisation)
        assert (response.status_code == 400 and
                response.json()['message'] == data.TestBodyText.text_courier_authorisation_400)

    @allure.description('Нельзя авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_fail_authorisation_with_non_existent_user(self):
        authorisation = {'login': 'Abc', 'password': 'abc'}
        response = requests.post(data.URL.URL_LOGIN, data=authorisation)
        assert (response.status_code == 404 and
                response.json()['message'] == data.TestBodyText.text_courier_authorisation_404)

