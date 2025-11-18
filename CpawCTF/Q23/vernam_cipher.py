def decode_vernam_cipher():
    # 暗号化されたデータ (暗号文)
    ciphertext = [
        0x7a, 0x69, 0x78, 0x6e, 0x62, 0x6f, 0x7c, 0x6b,
        0x77, 0x78, 0x74, 0x38, 0x38, 100
    ]

    # 暗号文を復号
    plaintext = [char ^ 0x19 for char in ciphertext]

    # 復号結果を文字列に変換して表示
    print("".join([chr(x) for x in plaintext]))

if __name__ == "__main__":
    decode_vernam_cipher()