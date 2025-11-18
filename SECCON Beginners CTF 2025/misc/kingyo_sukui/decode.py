import base64

encrypted_b64 = "CB0IUxsUCFhWEl9RBUAZWBM="
secret_key_b64 = "a2luZ3lvZmxhZzIwMjU="

# Base64 decode
encrypted = base64.b64decode(encrypted_b64)
key = base64.b64decode(secret_key_b64)

# XOR復号
decrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(encrypted)])
print(decrypted.decode())
