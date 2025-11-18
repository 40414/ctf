def transformation(input_str):
    input_len = len(input_str) + 1

    transformed_str1 = [None] * input_len
    transformed_str2 = [None] * input_len

    for i in range(len(input_str)):
        char = input_str[i]
        transformed_char = (ord(char) << 3 & 0xFF) | (ord(char) >> 5)

        if transformed_char & 1 == 0:
            transformed_str1[i] = transformed_char & 0xCC
            transformed_str2[i] = transformed_char & 0x33
        else:
            transformed_str1[i] = transformed_char & 0x33
            transformed_str2[i] = transformed_char & 0xCC

    # Convert transformed byte arrays back to strings
    transformed_str1 = ''.join(chr(c) for c in transformed_str1 if c is not None)
    transformed_str2 = ''.join(chr(c) for c in transformed_str2 if c is not None)

    return transformed_str1, transformed_str2

def reverse_transformation(enc1, enc2):
    input_len = len(enc1)
    reversed_str = []

    for i in range(input_len - 1):  # 最後のバイトは終了文字なので無視
        if enc1[i] & 0xCC == enc1[i]:  # transformed_str1[i] に対応
            transformed_char = enc1[i] | (enc2[i] & 0x33)
        else:  # transformed_str2[i] に対応
            transformed_char = enc2[i] | (enc1[i] & 0x33)

        # 逆演算で元の文字を復元
        original_char = (transformed_char >> 3) | ((transformed_char & 0x07) << 5)
        reversed_str.append(chr(original_char & 0xFF))

    return ''.join(reversed_str)

def main():
    enc1 = bytes([
        0x08, 0x23, 0x03, 0x03, 0x13, 0x03, 0x13, 0x03, 0x01, 0x23,
        0x31, 0x13, 0x11, 0xC8, 0x03, 0xC8, 0x03, 0x13, 0x01, 0xC8,
        0x13, 0x13, 0x03, 0x13, 0x13, 0x11, 0x13, 0x23, 0x00
    ])
    enc2 = bytes([
        0x02, 0x40, 0x80, 0x08, 0x08, 0x08, 0xC8, 0xC8, 0x80, 0x88,
        0x08, 0x80, 0x88, 0x32, 0x08, 0x32, 0x80, 0x80, 0x80, 0x32,
        0x08, 0x80, 0x08, 0x08, 0x48, 0x88, 0x80, 0xC8, 0x00
    ])

    # 逆変換実行
    original_str = reverse_transformation(enc1, enc2)
    print(f"Reversed string: {original_str}")
    
    # 変換実行
    transformed_str1, transformed_str2  = transformation(original_str)
    if transformed_str1 == enc1 and transformed_str2 == enc2:
        print("congratz")
    else:
        print("wrong")

if __name__ == "__main__":
    main()