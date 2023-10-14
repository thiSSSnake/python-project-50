import argparse


def gendiff_h():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    # Positional arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Optional arguments
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args
