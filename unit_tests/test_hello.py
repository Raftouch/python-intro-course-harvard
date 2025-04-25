from hello import hello


def test_default():
    assert hello() == "Hello, World"


def test_name():
    for name in ["Bob", "Ann", "Lucy"]:
        assert hello(name) == f"Hello, {name}"


# pytest unit_tests