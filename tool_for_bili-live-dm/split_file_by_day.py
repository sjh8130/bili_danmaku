import sys
import time

from split_file_base import SPLIT_SEL, split_file_by_time

if __name__ == "__main__":
    st = time.time()
    item = sys.argv[1:]
    b_name = item[0]
    for i in item:
        split_file_by_time(i, b_name, SPLIT_SEL.DAY)
    print(time.time() - st)
