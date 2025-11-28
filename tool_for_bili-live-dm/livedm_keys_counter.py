import json
import os
import sys
import time
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json

import livedm_keys_counter_lib
from tqdm import tqdm


def _main():
    n = "livedm_keys.json"
    if True and (a := (output_dir / n)).exists():
        with a.open(encoding="utf-8") as fp:
            livedm_keys_counter_lib.result.update(simdjson.load(fp))
    for path_s in tqdm(paths, leave=False):
        if not output_dir.exists():
            output_dir.mkdir()
        if (path := Path(path_s)) == output_dir:
            continue
        livedm_keys_counter_lib.p_main(path)
    with a.open("w", encoding="utf-8") as fp:
        json.dump(livedm_keys_counter_lib.result, fp, ensure_ascii=False, indent="\t", sort_keys=True)


if __name__ == "__main__":
    paths = sys.argv[1:]
    output_dir = Path("Z:\\") if os.name == "nt" else Path("/mnt/z/")
    start_time = time.time()
    _main()
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    time.sleep(10)
