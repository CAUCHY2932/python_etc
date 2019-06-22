import allure
import pytest




@pytest.mark.skip()
def test_1():
    assert 1


@pytest.mark.xfail()
def test_2():
    assert 1


def test_3():
    assert 1


class TestClass(object):
    def test_4(self):
        with allure.step("测试test_4"):
            allure.attach("期望值是hahahh")
            assert 0



@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
    ({"a": "中文"}, {"a": 1})
], ids=["中文测试用例", "中文和eving", "6*9", "dict compare"])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

class TestClass(object):
    @pytest.mark.parametrize("test_input,expected", [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 42),
        ({"a": "中文"}, {"a": 1})
    ], ids=["中文测试用例", "中文和eving", "6*9", "dict compare"])
    def test_classssssss(self, test_input, expected):
        assert eval(test_input) == expected
