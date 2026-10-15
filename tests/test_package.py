import importlib.resources

import varistor


def test_package_is_typed() -> None:
    assert importlib.resources.files(varistor).joinpath("py.typed").is_file()
