# coding=utf-8

import sys

def read_input(file):
    for line in file:
        yield line.split()

def main():
    data = read_input(sys.stdin)

    for words in data:
        for word in words:
            print(f'{word}\t1')


