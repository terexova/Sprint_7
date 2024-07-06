import allure
import requests
import random
import data
from faker import Faker

@allure.step('Создание нового курьера')
def generate_registration():
    fake = Faker()
    login_pass = []

    login = fake.name()
    password = fake.password(9)
    first_name = fake.first_name()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(data.URL.URL_COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return login_pass

@allure.step('Данные для регистрации курьера')
def create_new_courier():
    fake = Faker()
    payload = {
        "login": fake.email(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }
    return payload


@allure.step('Удаление курьера')
def delete_courier(authorisation):
    response = requests.post(data.URL.URL_LOGIN, data=authorisation)
    courier_id = str(response.json()['id'])
    delete_response = requests.delete(data.URL.URL_DELETE + courier_id, data={'id': courier_id})
    assert delete_response.status_code == 200


def generate_order_details():
    fake = Faker()
    payload = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": 2,
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 10),
        "deliveryDate": "2024-06-26",
        "comment": "Can you bring it back after 2 p.m.?",

    }
    return payload