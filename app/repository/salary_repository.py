import pandas as pd

salary_dataset = pd.read_csv('app/db/salary_survey.csv')

columns = set(salary_dataset.columns)


def filter_column_by_condition(dataset, column_name, condition, value):
    if condition == '[gte]':
        return dataset.loc[dataset[column_name] >= value]
    if condition == '[gt]':
        return dataset.loc[dataset[column_name] > value]
    if condition == '[lte]':
        return dataset.loc[dataset[column_name] <= value]
    if condition == '[lt]':
        return dataset.loc[dataset[column_name] < value]

    return dataset.loc[dataset[column_name] == value]


def sort_dataset(dataset, values):
    return dataset.sort_values(by=values)


def truncate_columns(dataset, fields):
    return dataset.filter(items=fields)
