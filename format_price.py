import locale
import argparse
import string
import logging


logging.basicConfig(filename="format_price.log",
                    level=logging.DEBUG,
                    format="%(levelname)s:[%(asctime)s]:%(message)s")


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module for format price.')
    parser.add_argument(
        'price',  help='Where get the price.')
    return parser


def format_price(price):
    set_price = set(price)
    punctuation = set(string.punctuation)
    letters = set(string.ascii_letters)
    whitespace = set(string.whitespace)
    for pattern in (whitespace, letters, punctuation):
        if pattern & set_price:
            return logging.debug('Invalid data type, enter int!')
            break
    return '{:,}'.format(int(price)).replace(',', ' ')


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print(format_price(namespace.price))
