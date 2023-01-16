import file_reader
from caller import *
from constant import Constant

if __name__ == '__main__':
    Constant.iterations = 3
    Constant.interval_delay = 10  # sec

    generate_shared_context()
    generate_separate_context()
