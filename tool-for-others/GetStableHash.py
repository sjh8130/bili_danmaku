from functools import lru_cache


@lru_cache
def GetStableHash(str_input):
    hash1 = 5381
    hash2 = hash1
    for i in range(0, len(str_input), 2):
        if i < len(str_input):
            hash1 = ((hash1 << 5) + hash1) ^ ord(str_input[i])
            if i + 1 < len(str_input):
                hash2 = ((hash2 << 5) + hash2) ^ ord(str_input[i + 1])
    return (hash1 + (hash2 * 1566083941)) & 0x7FFFFFFF


if __name__ == "__main__":
    while True:
        print(GetStableHash(input()))
