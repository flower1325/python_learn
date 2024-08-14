import json
import base64
import jsonpath
import requests
from Crypto.Cipher import AES


class EncryptDate:  # AES
    def __init__(self, key):
        self.key = key.encode("utf-8")  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化 AES，ECB 模式的实例，可以选择其他模式

    def pad(self, text):
        # 填充函数，使被加密数据的字节码长度是 block_size 的整数倍
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, decrData):  # 加密函数
        res = self.aes.encrypt(self.pad(decrData).encode("utf-8"))
        # Base64 是网络上最常见的用于传输 8Bit 字节码的编码方式之一
        return base64.b64encode(res).decode("utf-8")

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf-8"))
        msg = self.aes.decrypt(res).decode("utf-8")
        return self.unpad(msg)

    def unpad(self, date):
        return date[0:-ord(date[-1])]


if __name__ == "__main__":
    print("======加密=====")
    key: str = '1234567812345678'
    data = "tony"
    eg = EncryptDate(key)
    res = eg.encrypt(str(data))
    print(res)
    data1 = "123456"
    res2 = eg.encrypt(str(data1))
    print(res2, end='      ')
    print("\n======解密=====")
    res3 = eg.decrypt("XbXHJrNLwoTVcyfqM9eTgQ==")
    print(res3)
