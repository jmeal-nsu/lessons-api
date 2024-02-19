import pytest


class TestHealthCheck:
    def test_one_devided_by_zero_is_zero_devision_exception(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
