#!/usr/bin/python

d = {}

d['key'] = 'value'
print(d['key'])

del d['key']
print(d['key'])

if 'key' in d:
    print(d['key'])
else:
    print("key doesn't exist")

