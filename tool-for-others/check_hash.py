import json
import os
from hashlib import md5

path = "G:\\xxx"
with open("Z:\\0", "r", -1, "utf-8") as hash:
    for itm in hash.readlines():
        pos = itm.find("{")
        name = itm[0:pos]
        hash = json.loads(itm[pos:])["ETag"]
        if os.path.exists(f"{path}\\{name}.ts"):
            with open(f"{path}\\{name}.ts", "rb") as file:
                if md5(file.read()).hexdigest() != hash:
                    print(name, "Checksum Fail")
        else:
            print(name, "not exist")
