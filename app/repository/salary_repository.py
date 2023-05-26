import pandas as pd

try:
    salary_dataset = pd.read_csv('app/db/salary_survey.csv')
except Exception as exception:
    salary_dataset = pd.read_csv('../db/salary_survey.csv')

columns = set(salary_dataset.columns)


def filter_dataset(conditions):
    return salary_dataset.query(' & '.join(conditions))


def sort_dataset(dataset, values):
    return dataset.sort_values(by=values)


def truncate_columns(dataset, fields):
    return dataset.filter(items=fields)
