from Crypto.Util.number import inverse, long_to_bytes

n = 272361880253535445317143279209232620259509770172080133049487958853930525983846305005657
c = 69147423377323669983172806367084358432369489877851180970277804462365354019444586165184
e = 65537

# 完全な立方数 n = p^3 から p を求めるための整数立方根（binary search 方式）
def integer_cube_root(x):
    lo = 0
    hi = 1 << ((x.bit_length() + 2) // 3)  # 適当な上界
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**3 < x:
            lo = mid + 1
        else:
            hi = mid
    # lo^3 == x なら p を返す
    if lo**3 == x:
        return lo
    else:
        raise ValueError("n is not a perfect cube")

# 3乗根して p を求める
p = integer_cube_root(n)

# RSAの秘密鍵を計算
# n = p^3 の場合、素因数分解が容易なので φ(n) = p^3 - p^2 = p^2 * (p - 1)
phi = p**2 * (p - 1)
d = inverse(e, phi)

# 復号: m = c^d mod n
m = pow(c, d, n)

flag = long_to_bytes(m)
print(f"flag = {flag.decode()}")