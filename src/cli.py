# command line interface
import argparse


# не понимаю, как протестировать этот модуль
# хотя он использует только стандартные библиотеки и непонятно зачем его тестировать
def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='first file')
    parser.add_argument('second_file', help='second file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()
