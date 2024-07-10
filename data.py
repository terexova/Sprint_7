class TestBodyText:
    text_courier_409 = 'Этот логин уже используется. Попробуйте другой.'
    text_courier_400 = 'Недостаточно данных для создания учетной записи'
    text_courier_authorisation_400 = 'Недостаточно данных для входа'
    text_courier_authorisation_404 = 'Учетная запись не найдена'

class TestBodyData:
    body_data_without_login = {'login': '',
                               'password': '123',
                               'firstName': 'Olga'
                               }

    body_data_without_password = {'login': 'terexova',
                                  'password': '',
                                  'firstName': 'Olga'
                                  }

    body_data_authorisation = {'login': 'Abc',
                               'password': 'abc'
                               }
