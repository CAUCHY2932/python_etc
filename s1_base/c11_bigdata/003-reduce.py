# coding=utf-8

import sys
from operator import itemgetter
from itertools import groupby

def read_mapper_output(file,separator='\t'):
    for line in file:
        yield line.rstrip().split(separator,1)

def main():
    data=read_mapper_output(sys.stdin)

    for current_word,group in groupby(data,itemgetter):
        total_count=sum(int(current_word))