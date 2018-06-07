#!/usr/bin/python

def test():
    result_string = ''
    for i in range(10):
        result_string = result_string + 'Hello world!<br>'
    return result_string

if __name__ == '__main__':
    print test()
