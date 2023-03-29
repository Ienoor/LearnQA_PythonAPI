import pytest
import requests


class TestUserAuth:
    def test_user_auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post('https://playground.learnqa.ru/api/user/login', data)
        assert "auth_sid" in response.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response.headers, "There is no CSRF token header in the response"
        assert "user_id" in response.json(), "There is no user id in the response"

        auth_sid = response.cookies.get('auth_sid')
        token = response.headers.get('x-csrf-token')
        user_id_from_auth_method = response.json()['user_id']

        response = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        assert "user_id" in response.json(), "There is no user id in the second response"
        user_id_from_check_method = response.json()['user_id']

        assert user_id_from_auth_method == user_id_from_check_method, \
            "User id from auth method is not equal to user id from check method"

    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post('https://playground.learnqa.ru/api/user/login', data)
        assert "auth_sid" in response.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response.headers, "There is no CSRF token header in the response"
        assert "user_id" in response.json(), "There is no user id in the response"

        auth_sid = response.cookies.get('auth_sid')
        token = response.headers.get('x-csrf-token')

        if condition == 'no_cookie':
            response = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={'x-csrf-token': token},
            )
        else:
            response = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={'auth_sid': auth_sid}
            )
        assert 'user_id' in response.json(), "There is no user id in the second response"
        user_id_from_check_method = response.json()['user_id']
        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"