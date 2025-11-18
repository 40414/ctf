import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def find_device_id():
    value1 = "99999991"
    ans = "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5"

    try:
        for i in range(10000000):  # 0 から 9999999 までループ
            # 7桁になるように0埋めする
            value2 = f"{i:07d}"
            device_id = value1 + value2
            
            # SHA-256ハッシュを計算
            sha256 = hashlib.sha256(device_id.encode()).hexdigest()
            
            # ハッシュが一致するか確認
            if sha256 == ans:
                return device_id
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_file(device_id):
    input_file = "./Jewel_c.png"
    output_file = "./Jewel_c_decrypt.png"

    try:
        # ファイルを読み込む
        with open(input_file, "rb") as f:
            encrypted_data = f.read()

        # 暗号化キーとIVを設定
        secret_key = ("!" + device_id).encode("ascii")
        iv = "kLwC29iMc4nRMuE5".encode("ascii")

        # AES復号化設定
        cipher = AES.new(secret_key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # 復号化したデータを出力ファイルに保存
        with open(output_file, "wb") as f:
            f.write(decrypted_data)

        print(f"Decryption successful. Output saved to: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    decrypt_file(find_device_id())