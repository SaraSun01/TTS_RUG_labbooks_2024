from assignments.S1.task import parse_phone_number, parse_url

def test_phone_parsing(test_data_1):
    title = test_data_1["title"]
    data = test_data_1["data"]
    solution = test_data_1["solution"]
    result = parse_phone_number(data)
    if isinstance(solution, list) and isinstance(result, list):
        assert sorted(result) == sorted(solution), f"Incorrect result in {title}"
    else:
        assert result == solution, f"Incorrect result in {title}"

def test_url_parsing(test_data_2):
    title = test_data_2["title"]
    data = test_data_2["data"]
    solution = test_data_2["solution"]
    result = parse_url(data)
    if isinstance(solution, list) and isinstance(result, list):
        assert sorted(result) == sorted(solution), f"Incorrect result in {title}"
    else:
        assert result == solution, f"Incorrect result in {title}"
