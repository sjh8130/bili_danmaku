import sys
import time
from pathlib import Path

from split_file_base import SplitMode, split_file_by_time

if __name__ == "__main__":
    st = time.time()
    item = sys.argv[1:]
    b_name = item[0]
    for i in item:
        split_file_by_time(Path(i), Path(b_name), SplitMode.M)
    print(time.time() - st)
