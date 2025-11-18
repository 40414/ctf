import struct

def fun_transform(block, key):
    """
    `FUN_00101272` に相当する関数: 入力ブロックを変換する。
    :param block: 4バイト整数 (uint32)
    :param key: バイト列でのキー
    :return: 変換された 4バイト整数
    """
    # サンプル変換 (XOR を使った簡易処理)
    transformed = block ^ struct.unpack("<Q", key[:8])[0]  # 最初の8バイトでXOR
    return transformed & 0xFFFFFFFF  # 32ビットに制限

def fun_main(argc, argv):
    """
    メイン関数のPython版。
    :param argc: コマンドライン引数の数
    :param argv: コマンドライン引数のリスト
    """
    # スタック保護を仮定
    stack_canary = 0x12345678ABCDEF00

    # 固定データ (キー)
    key_part1 = b"AlpacaHa"
    key_part2 = b"ckRound8"
    key = key_part1 + key_part2

    # 引数チェック
    if argc < 2:
        print(f"Usage: {argv[0]} <input>")
        return

    # 入力データの取得
    input_data = argv[1]
    input_length = len(input_data)

    # メモリの確保とブロック単位の準備
    blocks = (input_length + 3) // 4  # 4バイト単位に切り上げ
    buffer = bytearray(blocks * 4)  # 4バイト単位でブロック確保
    buffer[:input_length] = input_data.encode()  # 入力データをバッファにコピー

    # 入力の変換
    for i in range(blocks):
        block = struct.unpack_from("<I", buffer, i * 4)[0]  # 4バイト読み取り (リトルエンディアン)
        transformed = fun_transform(block, key)
        struct.pack_into("<I", buffer, i * 4, transformed)  # 変換結果を書き戻し

    # 比較対象データ (ハードコードされたバイト列)
    target_data = b"\x12\x34\x56\x78" * blocks  # 仮の比較データ
    if buffer[:len(target_data)] == target_data:
        print("congratz")
    else:
        print("wrong")

    # スタック保護チェック
    if stack_canary != 0x12345678ABCDEF00:
        raise RuntimeError("Stack smashing detected!")

# テスト実行
if __name__ == "__main__":
    # テスト用の引数リスト
    argv = ["program_name", "example_input"]
    fun_main(len(argv), argv)
