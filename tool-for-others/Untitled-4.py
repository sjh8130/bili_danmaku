J = open("D:\\1.gif", "rb").read()
P = open("D:\\1.png", "rb").read()
G = open("D:\\1.gif", "rb").read()
W = open("D:\\1.webp", "rb").read()

while True:
    pth = input()
    with open(pth, "rb") as fp:
        a = fp.read(12)
    if a.startswith(b"\x89PNG"):
        open(pth, "wb").write(P)
    elif a.startswith(b"GIF8"):
        open(pth, "wb").write(G)
    elif a.startswith(b"RIFF") and a.endswith(b"WEBP"):
        open(pth, "wb").write(W)
    elif a.startswith((b"\xff\xd8\xff\xe0", b"\xff\xd8\xff\xe1")):
        open(pth, "wb").write(J)
