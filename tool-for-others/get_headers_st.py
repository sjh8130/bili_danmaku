import requests

base = "https://dqrpb9wgowsf5.cloudfront.net/28ac040aeefa738494ac_sweetily_42555921422_1713243633/chunked/"
session = requests.Session()
for i in [4874]:
	a = session.head(f"{base}{i}.ts")
	print(f"{i}{a.headers}")