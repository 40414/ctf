# 条件に基づいてフラグを逆算するスクリプト

# 条件（例として利用する値）
conditions = [125, 114, 51, 75, 99, 52, 104, 95, 101, 84, 49, 72, 119, 95, 82, 95, 85, 123, 110, 115, 117, 115, 97]

# フラグ文字列を計算
flag = ""
for condition in conditions:
    # 各条件を逆算してASCIIコードを求める
    character = condition  # ここに適切な逆算式を挿入する
    flag += chr(character)

flag = flag[::-1]  # 逆順にする
print(f"Flag: {flag}")