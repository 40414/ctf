import requests
import hashlib

# Authorizationヘッダ作成に用いるパラメタ
url = "http://ctfq.u1tramarine.blue/q9/flag.html"
md5a1 = "c627e19450db746b739f41b64097d449"
nonce = ""
nc = ""
cnonce = ""
qop = "auth"
a2 = "GET:/q9/flag.html"
md5a2 = "9e2b6bca5d4d92f6ead358623df264c8"
username = "q9"
realm = "secret"
algorithm = "MD5"
uri = "/q9/flag.html"

#urlにアクセスして得られた応答のheader情報(WWW-Authenticate)からnonceを抜き出す。
auth_header = requests.get(url).headers['WWW-Authenticate']
nonce = auth_header.split(" ")[2][7:-2]

# responseの計算
not_md5_response = md5a1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + md5a2
md5_response = hashlib.md5(not_md5_response.encode('utf-8')).hexdigest()

#header情報の作成
#headerの形式はhttpストリームの3.に示したAuthrizationの形式に合わせる
headers  = {
    'Authorization': \
        'Digest username="' + username + '"' + ', ' + \
        'realm="' + realm + '"' + ', ' + \
        'nonce="' + nonce + '"' + ', ' + \
        'uri="' + uri + '"' + ', ' + \
        'algorithm="' + algorithm + '"' + ', ' + \
        'response="' + md5_response + '"' + ', ' + \
        'qop=' + qop + ', ' + \
        'nc=' + nc + ', ' + \
        'cnonce="' + cnonce + '"'
}

#作成したheader情報をurlに送信する
answer = requests.get(url, headers=headers)
print(answer.text)
