import json
import os
import sys
import time

import livedm_keys_counter_lib

if __name__ == "__main__":
    in_path = sys.argv[1:]
    if os.name == "nt":
        output_dir = "Z:\\"
    else:
        output_dir = "/mnt/z/"
    # if os.path.exists(os.path.join(output_dir, "result.json")):
    #     with open(os.path.join(output_dir, "result.json"), "r", encoding="utf-8") as fp:
    #         livedm_keys_counter_lib.result.update(json.load(fp))
    start_time = time.time()
    livedm_keys_counter_lib.main(in_path, output_dir)
    with open(os.path.join(output_dir, "result.json"), "w", encoding="utf-8") as fp:
        json.dump(livedm_keys_counter_lib.result, fp, ensure_ascii=False, indent="\t")
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    # print("TIME ", (os.stat(in_path[0]).st_size / 1024**2) / total_time)
    # time.sleep(10)
