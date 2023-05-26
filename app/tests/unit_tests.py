import unittest

from app.service.salary_service import check_fields_for_operation, parse_column_and_condition, column_is_present, \
    operation_is_support, pretty_value, obtain_condition


class Test(unittest.TestCase):

    def test_check_fields_for_operation(self):
        result = check_fields_for_operation('Timestamp,Company Name')
        self.assertTrue(result)

        result = check_fields_for_operation(None)
        self.assertFalse(result)

        result = check_fields_for_operation('Timestamp, Company Name')
        self.assertFalse(result)

    def test_parse_column_and_condition(self):
        result_column, result_condition = parse_column_and_condition('Timestamp[gte]')
        self.assertEqual(result_column, 'Timestamp')
        self.assertEqual(result_condition, '[gte]')

        result_column, result_condition = parse_column_and_condition('Timestamp[ge]')
        self.assertIsNone(result_column)
        self.assertIsNone(result_condition)

        result_column, result_condition = parse_column_and_condition('Timestamp')
        self.assertEqual(result_column, 'Timestamp')
        self.assertEqual(result_condition, '')

    def test_column_is_present(self):
        result = column_is_present('Timestamp')
        self.assertTrue(result)

        result = column_is_present('Custom')
        self.assertFalse(result)

    def test_operation_is_support(self):
        result = operation_is_support('fields')
        self.assertTrue(result)

        result = operation_is_support('custom')
        self.assertFalse(result)

    def test_pretty_value(self):
        result = pretty_value('')
        self.assertIsNone(result)

        result = pretty_value('10')
        self.assertEqual(result, float(10))

        result = pretty_value('test')
        self.assertEqual(result, 'test')

    def test_obtain_condition(self):
        result = obtain_condition('[gte]')
        self.assertEqual(result, '>=')

        result = obtain_condition('[gt]')
        self.assertEqual(result, '>')

        result = obtain_condition('[lte]')
        self.assertEqual(result, '<=')

        result = obtain_condition('[lt]')
        self.assertEqual(result, '<')

        result = obtain_condition('')
        self.assertEqual(result, '==')

        result = obtain_condition(None)
        self.assertEqual(result, '==')

        result = obtain_condition('test')
        self.assertEqual(result, '==')
