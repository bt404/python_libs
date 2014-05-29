# -*- coding: utf-8 -*-

# must return an object in __enter__ when use
# with statement. order of invocation :
# __enter__ --> with block --> __exit__
class Sample(object):
    def __enter__(self):
        print "In __enter__"
        return self

    def __exit__(self, type, value, trace):
        print "In __exit__"
        print "type: ", type
        print "value: ", value
        print "trace: ", trace

    def bad_division(self):
        print "during exec"
        ret = 2/0   # raise exception


if __name__ == "__main__":
    with Sample() as sample:
        sample.bad_division()
    #with open('not exists') as sample:  # with don't try exception before going into block
    #    sample.read()
