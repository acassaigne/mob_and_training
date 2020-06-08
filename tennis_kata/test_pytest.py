
import pytest


class TestTennis:

    @pytest.mark.parametrize('param1 param2'.split(), [("un", "deux")])
    def test_get_score_game1(self, param1, param2):
        print(f"param1={param1}")
        print(param2)
        assert param1 == "un"
        assert param2 == "deux"
