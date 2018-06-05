#!/usr/bin/python
import urllib2

url = 'https://raw.githubusercontent.com/kristjankorjus/nodeploy_test/master/test.py'
response = urllib2.urlopen(url)
python_script = response.read()

__name__ = 'random'

exec(python_script)

print test()
