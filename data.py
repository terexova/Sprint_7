class URL:
    URL_BASE = 'https://qa-scooter.praktikum-services.ru/'
    URL_COURIER = f'{URL_BASE}/api/v1/courier'
    URL_LOGIN = f'{URL_BASE}/api/v1/courier/login'
    URL_DELETE = f'{URL_BASE}/api/v1/courier/'
    URL_ORDER = f'{URL_BASE}/api/v1/orders'

class TestBodyText:
    text_courier_409 = 'Этот логин уже используется. Попробуйте другой.'
    text_courier_400 = 'Недостаточно данных для создания учетной записи'
    text_courier_authorisation_400 = 'Недостаточно данных для входа'
    text_courier_authorisation_404 = 'Учетная запись не найдена'




