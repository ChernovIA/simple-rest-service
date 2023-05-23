import re

import app.repository.salary_repository as repo

LEFT_BRACKET = '['
SORT_OPERATION = 'sort'
FIELDS_OPERATION = 'fields'
ADDITIONAL_OPERATIONS = {SORT_OPERATION, FIELDS_OPERATION}


def process_request(args):
    dataset = repo.salary_dataset
    filter_operations = []
    additional_operations = dict()
    for param, value in args.items():
        value = pretty_value(value)
        if column_is_present(param):
            column_name, condition = parse_column_and_condition(param)
            if column_name is not None:
                str_value = '"' + value + '"' if isinstance(value, str) else str(value)
                filter_operations.append(
                    f'`{column_name}` {obtain_condition(condition)} {str_value}'
                )

        elif operation_is_support(param) and check_fields_for_operation(value):
            additional_operations[param] = value.split(',')

    if len(filter_operations) > 0:
        dataset = repo.filter_dataset(filter_operations)

    if additional_operations.get(SORT_OPERATION) is not None:
        dataset = repo.sort_dataset(dataset, additional_operations[SORT_OPERATION])

    if additional_operations.get(FIELDS_OPERATION) is not None:
        dataset = repo.truncate_columns(dataset, additional_operations[FIELDS_OPERATION])

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
    return column_name in repo.columns


def operation_is_support(operation_name):
    return operation_name in ADDITIONAL_OPERATIONS


def pretty_value(value):
    if value.strip() == '':
        return None
    if value.isnumeric():
        return float(value)
    return value


def obtain_condition(condition):
    if condition == '[gte]':
        return '>='
    if condition == '[gt]':
        return '>'
    if condition == '[lte]':
        return '<='
    if condition == '[lt]':
        return '<'

    return '=='
