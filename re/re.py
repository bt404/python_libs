# -*- coding: utf-8 -*-
import re


def get_content(file_name):
    with open(file_name) as my_file:
        content = my_file.read()
    return content


def log_parser():
    content = get_content("doc.txt")


    num_selector = re.compile(r'\d{2}')
    result = num_selector.search(content)

    #result = re.search(r'is', content)
    print result


if __name__ == "__main__":
    log_parser()
    print 'test end'
