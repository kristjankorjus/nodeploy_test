#!/usr/bin/python

def test(a):
    result_string = ''
    for i in range(a):
        result_string = result_string + '<img src="https://img.buzzfeed.com/buzzfeed-static/static/2015-02/19/11/enhanced/webdr11/anigif_enhanced-6690-1424363569-2.gif" alt="Smiley face" height="42" width="42"><br>'
    return result_string

if __name__ == '__main__':
    print test(5)
