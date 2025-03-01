import json
import os
import sys
import time

try:
    import simdjson
except ImportError:
    simdjson = json

import livedm_keys_counter_lib
from tqdm import tqdm


def main():
    p1 = "livedm_keys.json"
    if True and os.path.exists(os.path.join(output_dir, p1)):
        with open(os.path.join(output_dir, p1), "r", encoding="utf-8") as fp:
            livedm_keys_counter_lib.result.update(simdjson.load(fp))
    for path in tqdm(paths, leave=False):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        if path == output_dir:
            continue
        livedm_keys_counter_lib.p_main(path)
    with open(os.path.join(output_dir, p1), "w", encoding="utf-8") as fp:
        json.dump(
            livedm_keys_counter_lib.result,
            fp,
            ensure_ascii=False,
            indent="\t",
            sort_keys=True,
        )


if __name__ == "__main__":
    paths = sys.argv[1:]
    if os.name == "nt":
        output_dir = "Z:\\"
    else:
        output_dir = "/mnt/z/"
    start_time = time.time()
    main()
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    time.sleep(10)
