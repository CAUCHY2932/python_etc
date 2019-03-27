# coding:utf-8

from xmlrpclib import ServerProxy, Fault

from cmd import Cmd

from string import lowercase

from server import Node, UNHANDLED

from time import sleep

HEAD_START=0.1

import sys

def randomString(length):
    char=[]
    letters=[]
    
