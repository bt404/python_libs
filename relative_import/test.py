# explict relative import test
# should notice file using explict relative import
# can't be execused directly
from rela.second import second

if __name__ == "__main__":
    second.show()
    print ''
