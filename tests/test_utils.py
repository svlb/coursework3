from utils import utils


def test_sort_by_data():
    assert utils.sort_by_data([{"date": "2018-08-17T03:57:28.607101"}, {"date": "2018-02-03T07:16:28.366141"}]) \
           == [{'date': '2018-08-17T03:57:28.607101'}, {'date': '2018-02-03T07:16:28.366141'}]
    assert utils.sort_by_data([{"date": "2018-08-17T03:57:28.607101"}, {}]) == [{"date": "2018-08-17T03:57:28.607101"}]
    assert utils.sort_by_data([{'date': '2018-08-17T03:57:28.607101'}, {'data': '2018-02-03T07:16:28.366141'}]) == [{'date': '2018-08-17T03:57:28.607101'}]
    assert utils.sort_by_data([{'date': None}, {'date': '2018-02-03T07:16:28.366141'}]) == [{'date': '2018-02-03T07:16:28.366141'}]


def test_time_conversion():
    assert utils.time_conversion('2018-08-17T03:57:28.607101') == '17.08.2018'


def test_mask_number():
    assert utils.mask_number("Счет 11492155674319392427") == "Счет  **2427"
    assert utils.mask_number("Maestro 1913883747791351") == "Maestro  1913 88** **** 1351"



def test_filter_by_executed():
    assert utils.filter_by_executed([{'state': "EXECUTED", "description": "Перевод организации"}, {'state': "CANCELED", "description": "Перевод организации"}]) == [{'description': 'Перевод организации', 'state': 'EXECUTED'}]
    assert utils.filter_by_executed([{'state': "EXECUTED", "description": "Перевод организации"},
                                     {'state': "EXECUTED", "description": "Перевод организации"},
                                     {'state': "EXECUTED", "description": "Перевод организации"},
                                     {'state': "EXECUTED", "description": "Перевод организации"},
                                     {'state': "EXECUTED", "description": "Перевод организации"}]) == [{'state': "EXECUTED", "description": "Перевод организации"},
                                     {'state': "EXECUTED", "description": "Перевод организации"},
                                    {'state': "EXECUTED", "description": "Перевод организации"},
                                     {'state': "EXECUTED", "description": "Перевод организации"},
                                     {'state': "EXECUTED", "description": "Перевод организации"}]

def test_get_formated_operation():
    assert utils.get_formated_operation(
        {'date': '2019-12-08T22:46:21.935582',
          'description': 'Открытие вклада',
          'id': 863064926,
          'operationAmount': {'amount': '41096.24',
                              'currency': {'code': 'USD', 'name': 'USD'}},
          'state': 'EXECUTED',
          'to': 'Счет 90424923579946435907'},
    ) == '''08.12.2019 Открытие вклада  \nСчет  **5907 \n41096.24 USD \n'''
    assert utils.get_formated_operation(
        {'date': '2019-12-07T06:17:14.634890',
         'description': 'Перевод организации',
         'from': 'Visa Classic 2842878893689012',
         'id': 114832369,
         'operationAmount': {'amount': '48150.39',
                             'currency': {'code': 'USD', 'name': 'USD'}},
         'state': 'EXECUTED',
         'to': 'Счет 35158586384610753655'}) == '''07.12.2019 Перевод организации  \nVisa Classic  2842 87** **** 9012 -> Счет  **3655 \n48150.39 USD \n'''