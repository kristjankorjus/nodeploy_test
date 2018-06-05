#!/usr/bin/python

with open('test.py', 'r') as f:
    read_data = f.read()

__name__ = 'random'

exec(read_data)

print test()
