"""
怎么发起请求？
第一个问题：
不同的接口请求方式不同。
反射方式  第一个参数，调用程序包（对象），第二参数，调用的具体函数（字符串）

老代码：
if "post" == method:
    getattr(request,"pos/get")


优化： 满足完成所有请求的调用，数据拆分（列表的形式）

requests.request(
    url=url,
    method=method,
    params=params,
    data=data,
    json=json,
    headers=headers,
)



"""
import requests


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
method = "post"
url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"


def send_request(url,headers,method,params, data):
    res = requests.request(
        url=url,
        headers=headers,
        params=params,
        method="post",
        data=data)
    print(res.text)

if __name__ == "__main__":
    send_request(url, headers,method, params, data)

