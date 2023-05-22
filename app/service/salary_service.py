import re

import app.repository.salary_repository as repo

LEFT_BRACKET = '['
ADDITIONAL_OPERATIONS = ['sort', 'fields']


def process_request(args):
    dataset = repo.salary_dataset
    additional_operations = []
    for param, value in args.items():
        value = pretty_value(value)
        if column_is_present(param):
            column_name, condition = parse_column_and_condition(param)
            if column_name is not None:
                dataset = repo.filter_column_by_condition(dataset, column_name, condition, value)

        elif operation_is_support(param) and check_fields_for_operation(value):
            additional_operations.append({
                'type': param,
                'value': value.split(',')
            })

    for operation in additional_operations:
        if operation['type'] == ADDITIONAL_OPERATIONS[0]:
            dataset = repo.sort_dataset(dataset, operation['value'])
        if operation['type'] == ADDITIONAL_OPERATIONS[1]:
            dataset = repo.truncate_columns(dataset, operation['value'])

    return dataset.fillna('').to_dict(orient='records')


def check_fields_for_operation(values):
    if values is None:
        return False

    for value in values.split(','):
        if value not in repo.columns:
            return False

    return True


def parse_column_and_condition(column_name):
    reg_exp = r'\[(gte|gt|lte|lt)\]$'
    match = re.search(reg_exp, column_name)
    if match:
        condition = match.group()
        return column_name.split(LEFT_BRACKET)[0].strip(), condition
    if LEFT_BRACKET in column_name:
        return None, None

    return column_name, ''


def column_is_present(column_name):
    column_name = column_name.split(LEFT_BRACKET)[0].strip()
    if column_name in repo.columns:
        return True
    return False


def operation_is_support(operation_name):
    if operation_name in ADDITIONAL_OPERATIONS:
        return True
    return False


def pretty_value(value):
    if value.strip() == '':
        return None
    if value.isnumeric():
        return float(value)
    return value