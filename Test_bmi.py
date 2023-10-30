import Lab2.bmi as bmi

def test_bmi_under_weight():
    input_weight = 37
    input_height = 1.73
    correctans = -1
    result = bmi.calculate_bmi(input_height,input_weight)
    assert (result == correctans)
def test_bmi_normal_weight():
    input_weight = 57
    input_height = 1.73
    correctans = 0
    result = bmi.calculate_bmi(input_height,input_weight)
    assert (result == correctans)
def test_bmi_over_weight():
    input_weight = 87
    input_height = 1.73
    correctans = 1
    result = bmi.calculate_bmi(input_height,input_weight)
    assert (result == correctans)