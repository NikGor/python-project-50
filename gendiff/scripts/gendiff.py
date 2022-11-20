#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# gendiff -h
# usage: gendiff [-h] first_file second_file
#
# Compares two configuration files and shows a difference.
#
# positional arguments:
#   first_file
#   second_file
#
# optional arguments:
#   -h, --help            show this help message and exit


import argparse
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
args = parser.parse_args()


def main():
    pass


if __name__ == '__main__':
    main()
