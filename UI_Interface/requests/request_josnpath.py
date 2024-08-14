import requests
import jsonpath
import Crypto.Cipher

from UI_Interface.AES.AES加密解密 import EncryptDate

data = {
    "accounts": "huace_tester",
    "pwd": "huace_tester",
    "type": "username"
}

params = {
    "application": "app",
    "application_client_type": "weixin"
}
headers = {
    "application": "app",
    "application_client_type": "weixin"
}

rs = requests.post(
    url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",
    headers=headers,
    params=params,
    data=data,
)
print(rs.text)

"""
加入购物车
"""
data2 = {
    "goods_id": "2",
    "spec": [
        {
            "type": "套餐",
            "value": "套餐⼆"
        },
        {
            "type": "颜⾊",
            "value": "银⾊"
        },
        {
            "type": "容量",
            "value": "64G"
        }
    ],
    "stock": 2
}
token = rs.json()["data"]["token"]
print(token)
token_list = jsonpath.jsonpath(rs.json(), '$..token')
print(token_list[0])

rs2 = requests.post(
    url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save&token=" + format(token_list[0]),
    headers=headers,
    params=params,
    data=data2,
)
print(rs2.text)

data3 = {
    "id": "12"
}
rs3 = requests.post(
    url="http://shop-xo.hctestedu.com/index.php?s=api/goods/favor&token=" + format(token_list[0]),
    headers=headers,
    params=params,
    data=data3,
)
print(rs3.text)

""""
对称加密
"""
eg = EncryptDate("1234567891234567")
eg.encrypt()
print(eg.text)
