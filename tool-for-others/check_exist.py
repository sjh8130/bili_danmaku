import os
path = "G:\\v2121135230"
for i in range(0,11937):
	if not os.path.exists(f"{path}\\{i}.ts"):
		print(i)