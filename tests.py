import unittest
from format_price import format_price


class PriceIntTest(unittest.TestCase):
    def test_only_number(self):
        test_value = str('111')
        expected = str(111)
        number = format_price(test_value)
        self.assertEqual(expected, number)

    def test_begin_one_dot(self):
        test_value = str('.111')
        expected = str(0)
        number = format_price(test_value)
        self.assertEqual(expected, number)

    def test_end_one_dot(self):
        test_value = str('111.')
        expected = str(111)
        number = format_price(test_value)
        self.assertEqual(expected, number)

    def test_one_comma(self):
        test_value = str('111,')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)

    def test_one_dot_one_number(self):
        test_value = str('111.2')
        expected = str(111)
        number = format_price(test_value)
        self.assertEqual(expected, number)

    def test_one_comma_one_number(self):
        test_value = str('111,2')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)

    def test_two_dot(self):
        test_value = str('111.2.3')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)

    def test_two_comma(self):
        test_value = str('111,2,3')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)

    def test_one_dot_two_symbols(self):
        test_value = str('11%.@11')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)

    def test_one_comma_one_letter(self):
        test_value = str('1OO,a1')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)

    def test_one_symbol_one_letter(self):
        test_value = str('a$')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)

    def test_one_comma_two_letters(self):
        test_value = str('O.O')
        expected = TypeError
        number = format_price(test_value)
        self.assertRaises(expected, number)


if __name__ == "__main__":
    unittest.main()
