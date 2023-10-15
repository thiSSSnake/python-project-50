#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import parsing



def main():

    print(parsing())
    print(generate_diff('gendiff/file1.json', 'gendiff/file2.json'))


if __name__ == '__main__':

    main()
