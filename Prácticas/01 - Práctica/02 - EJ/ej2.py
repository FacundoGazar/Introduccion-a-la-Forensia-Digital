data = bytes.fromhex('1c08082b2d213e0f3b2b293426112d0f3e2b352d')
key = b'UNLP'
flag = bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
print(flag.decode())