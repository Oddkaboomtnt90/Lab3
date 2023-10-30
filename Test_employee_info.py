import employee_info


def test_get_employees_by_age_range():
    input_lower_limit = 35
    input_upper_limit = 50
    answer = [{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result = employee_info.get_employees_by_age_range(input_lower_limit,input_upper_limit)
    assert (result == answer)


def test_calculate_average_salary():
    input_employee_data = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}
    ]
    answer = 55000
    result = employee_info.calculate_average_salary(input_employee_data)
    assert (result == answer)


def test_get_employees_by_dept():
    input_department = "Marketing"
    answer = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result = employee_info.get_employees_by_dept(input_department)
    assert (result == answer)