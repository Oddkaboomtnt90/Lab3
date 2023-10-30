import price_info


def test_cost_of_fruits():
    input_fruit = 'orange'
    input_quantity = 2
    answer = 2.80
    result = price_info.cost_of_fruits(input_fruit,input_quantity)
    assert (result == answer)


def test_total_cost_shopping():
    input_price_list = {'plane': 9.90, 'car': 2.20, 'tower': 4.40}
    input_quantity_list = {'plane': 11, 'car': 10, 'tower': 10}
    answer = 174.9
    result = price_info.total_cost_shopping(input_price_list, input_quantity_list)
    assert (result == answer)

