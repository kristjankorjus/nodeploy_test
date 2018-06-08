#!/usr/bin/python

def test(a):
    result_string = ''
    for i in range(a):
        result_string = result_string + 'Hello world!<br>'
    return result_string

if __name__ == '__main__':
    print test(5)
