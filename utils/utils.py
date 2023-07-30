import json
from datetime import datetime


def read_data():
    with open('operations.json') as file:
        data_file = json.loads(file.read())
        return data_file


def sort_by_data(operations):
    valid_operations = []
    for operation in operations:
        if not operation:
            continue
        elif 'date'not in operation:
            continue
        elif not operation.get('date'):
            continue
        valid_operations.append(operation)
    sort = sorted(valid_operations, key=lambda elem: elem['date'], reverse=True)
    return sort


def filter_by_executed(operations):
    executed_operations = []
    for operation in operations:
        if operation['state'] == "EXECUTED":
            executed_operations.append(operation)
            if len(executed_operations) == 5:
                break
    return executed_operations


def time_conversion(date): # Получает строку
    date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date


def mask_number(bill_info):
    card_info = bill_info.split()
    number = card_info[-1]
    if bill_info.lower().startswith('счет'):
        masked_number = f' **{number[-4:]}'
    else:
        masked_number = f' {number[:4]} {number[4:6]}** **** {number[-4:]}'
    card_info[-1] = masked_number
    hidden_list_ = ' '.join(card_info)
    return hidden_list_


def get_formated_operation(operation):
    line_1 = ''
    my_date = time_conversion(operation['date'])
    line_1 += my_date + ' '
    line_1 += operation['description'] + ' '

    line_2 = ''
    from_info = operation.get('from')
    if from_info:
        hidden_info = mask_number(from_info)
        line_2 += hidden_info + ' -> '
    to_info = operation['to']
    hidden_to_info = mask_number(to_info)
    line_2 += hidden_to_info + ' '

    line_3 = ''
    line_3 += operation['operationAmount']['amount'] + ' '
    line_3 += operation['operationAmount']['currency']['name'] + ' '
    return f'''{line_1} 
{line_2}
{line_3}
'''
