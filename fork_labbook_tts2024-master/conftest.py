import json
import pytest
def pytest_addoption(parser):
    parser.addoption(
        "--test_data_1",
        action="store",
        default="",
        help="name of the file containing test data",
    )
    parser.addoption(
        "--test_data_2",
        action="store",
        default="",
        help="name of the second file containing test data",
    )

def pytest_generate_tests(metafunc):
    if "test_data_1" in metafunc.fixturenames:
        option = metafunc.config.getoption("test_data_1")
        test_data_1 = open(metafunc.config.getoption("test_data_1"))
        test_json_1 = json.load(test_data_1)
        metafunc.parametrize("test_data_1", test_json_1)
    if "test_data_2" in metafunc.fixturenames:
        test_data_2 = open(metafunc.config.getoption("test_data_2"))
        test_json_2 = json.load(test_data_2)
        metafunc.parametrize("test_data_2", test_json_2)