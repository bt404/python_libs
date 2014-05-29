# -*- coding: utf-8 -*-

class Sample(object):
    def __enter__(self):
        print "In __enter__"

    def __exit__(self, type, value, trace):
        print "In __exit__"
        print "type: ", type
        print "value: ", value
        print "trace: ", trace

    def error_open(self):
        file = open('notexists')
        content = file.read()

    def bad_division(self):
        ret = 2/0


if __name__ == "__main__":
    with Sample() as sample:
        sample.bad_division()
    with open('not exists') as sample:
        sample.read()
