checks = [
    (38, 0x7b), (20, 0x67), (46, 0x5f), (3, 0x21), (18, 0x63),
    (119, 0x6e), (51, 0x5f), (59, 0x79), (9, 0x34), (4, 0x57),
    (37, 0x35), (12, 0x33), (111, 0x62), (45, 0x63), (97, 0x7d),
    (54, 0x30), (112, 0x74), (106, 0x31), (43, 0x66), (17, 0x34),
    (98, 0x34), (120, 0x54), (25, 0x5f), (127, 0x6c), (26, 0x41),
]

def f_b(x):
    return 1024 + ((23 + 37 * (x ^ 0x5a5a)) % 101)

# f_b(index) => chr(ascii)
memory = [0] * 2048  # メモリの仮領域
for idx, asc in checks:
    
    addr = f_b(idx)
    memory[addr] = chr(asc)

# メモリの中身を出力（確認）
flag_core = ''.join(memory[1024:1049])
print(flag_core)
