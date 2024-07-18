#!/dev/null
from functools import lru_cache


BV_AV_table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
BV_AV_base58_dic = {}
for BV_AV_base58_i in range(58): BV_AV_base58_dic[BV_AV_table[BV_AV_base58_i]] = BV_AV_base58_i
s = [11, 10, 3, 8, 4, 6]
BV_AV_xor = 177451812
BV_AV_add = 8728348608


@lru_cache
def BV2AV(input_BV: str):
	"""
	Text
	"""
	result = 0
	for i in range(6): result += BV_AV_base58_dic[input_BV[s[i]]]*58**i
	aid = (result-BV_AV_add) ^ BV_AV_xor
	if aid <= 0 or aid >= 29460791296: print(f"[BV_to_AV]: {input_BV}")
	return aid


@lru_cache
def AV2BV(input_AV: int):
	"""
	Text
	"""
	if input_AV >= 29460791296: print(f"[AV_to_BV]: {input_AV}")
	input_AV = (input_AV ^ BV_AV_xor)+BV_AV_add
	result = list('BV1  4 1 7  ')
	for i in range(6): result[s[i]] = BV_AV_table[input_AV//58**i % 58]
	return ''.join(result)
