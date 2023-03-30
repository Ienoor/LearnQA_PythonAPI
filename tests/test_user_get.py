import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserGet(BaseCase):

    def test_get_user_details_not_auth(self):
        response = requests.get(f"https://playground.learnqa.ru/api/user/2")

        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_not_key(response, 'firstname')
        Assertions.assert_json_has_not_key(response, 'lastname')
        Assertions.assert_json_has_not_key(response, 'email')

    def test_get_user_details_auth_as_some_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post('https://playground.learnqa.ru/api/user/login', data)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_volue(response, 'user_id')

        response = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        expected_fields = [
            'username',
            'firstName',
            'lastName',
            'email'
        ]
        Assertions.assert_json_has_keys(response, expected_fields)

