from json import JSONDecodeError

from requests import Response


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name: str, expected_value, error_message: str) -> None:
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, user_id: str) -> None:
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert user_id in response_as_dict, f"Response JSON doesn't have key '{user_id}'"

    @staticmethod
    def assert_json_has_keys(response: Response, keys: list) -> None:
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for key in keys:
            assert key in response_as_dict, f"Response JSON doesn't have key '{key}'"

    @staticmethod
    def assert_status_code(response: Response, status_code: int) -> None:
        assert response.status_code == status_code, f"Unexpected status code {response.status_code}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name: str) -> None:
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"
