#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import parsing


def main():

    first_file, second_file = parsing()
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':

    main()
