import locale
import argparse
import string


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module for format price.')
    parser.add_argument(
        'price',  help='Where get the price.')
    return parser


def format_price(price):
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

    set_price = set(price)
    punctuation = set(string.punctuation) - set('.')
    letters = set(string.ascii_letters)
    whitespace = set(string.whitespace)
    for pattern in (whitespace, letters, punctuation):
        if pattern & set_price or price.count('.') > 1:
            return print('Invalid data type, enter int or float!')
            break
    return locale.format_string("%d", float(price), grouping=True)



if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print(format_price(namespace.price))
