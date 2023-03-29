from datetime import datetime

import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    email = 'vinkotov@example.com'

    def setup_method(self):
        base_path = 'learn'
        domain = 'example.com'
        random_path = datetime.now().strftime('%d%m%Y%H%M%S')

        self.email = f"{base_path}{random_path}@{domain}"

    def test_successful_user_creation(self):
        data = {
            'username': 'learn_qa',
            'firstName': 'learn_qa',
            'lastName': 'learn_qa',
            'email': self.email,
            'password': '123',
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_id(response, 'id')

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'username': 'learn_qa',
            'firstName': 'learn_qa',
            'lastName': 'learn_qa',
            'email': email,
            'password': '123',
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("UTF-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content '{response.content}'"
