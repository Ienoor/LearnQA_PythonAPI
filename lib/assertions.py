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
    def assert_json_has_id(response: Response, user_id: str) -> None:
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert user_id in response_as_dict, f"Response JSON doesn't have key '{user_id}'"

    @staticmethod
    def assert_status_code(response: Response, status_code: int) -> None:
        assert response.status_code == status_code, f"Unexpected status code {response.status_code}"
