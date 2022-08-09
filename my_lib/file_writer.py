import gzip
import tarfile
import os
import sys
import io


def writeE(filename: str, data, gz: bool = False, binary_: bool = False):
	if gz:
		io.TextIOWrapper(gzip.open(filename + ".gz", 'wb', compresslevel=9), encoding='utf-8').writelines(data)
	elif binary_:
		open(filename, "wb").write(data)
	else:
		open(filename, "w", encoding="utf-8").write(data)
