import argparse


def parsing_arguments():  # noqa: E501
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    # Positional arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    # Optional arguments
    parser.add_argument('-f', '--format',
                        default="stylish",
                        help='set format of output (default: "stylish")')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
