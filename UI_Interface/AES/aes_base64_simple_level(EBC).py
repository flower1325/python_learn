from Crypto.Cipher import AES
import base64

# 补位
pad = lambda s: s + chr(16 - len(s) % 16) * (16 - len(s) % 16)
# 除去补16字节的多余字符
unpad = lambda s: s[:-s[-1]]


# 加密函数
def aes_ECB_Encrypt(data, key):   # ECB模式的加密函数，data为明文，key为16字节密钥
    key = key.encode('utf-8')
    data = pad(data)             # 补位
    data = data.encode('utf-8')
    aes = AES.new(key=key, mode=AES.MODE_ECB)  # 创建加密对象
    # encrypt AES加密  B64encode为base64转二进制编码
    result = base64.b64encode(aes.encrypt(data))
    return str(result, 'utf-8')        # 以字符串的形式返回


key = '1qaz@WSXabcdefgh'  # 秘钥
data = "haha1234567890"   # 明文字符串
encrypt_data = aes_ECB_Encrypt(data, key)
print("待加密的字符是：{}\n秘钥为：{}\n加密后的密文为：{}".format(data, key, encrypt_data))

