class TestExample:
    def test_check_math(self):
        a = 5
        b = 4

        assert a + b == 9

    def test_check_math1(self):
        a = 5
        b = 4
        expected_sum = 4
        assert a + b == expected_sum, "Должно быть 9"
