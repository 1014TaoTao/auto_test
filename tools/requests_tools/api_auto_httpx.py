# 二次封装httpx



"""好的，以下是使用Python封装httpx模块不同HTTP请求方式的示例代码：
这个示例代码包含了常见的HTTP请求方式：
    GET、POST、PUT、DELETE和OPTIONS，并且也提供了一个通用的`request`方法，可以满足其他HTTP请求的需求。您可以根据实际需求修改这个代码来满足您的需求。
"""


import httpx

class HttpxWrapper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.client = httpx.Client()
   
    def get(self, url, params=None, **kwargs):
        response = self.client.get(self.base_url + url, params=params, **kwargs)
        return response
   
    def post(self, url, data=None, **kwargs):
        response = self.client.post(self.base_url + url, data=data, **kwargs)
        return response
   
    def put(self, url, data=None, **kwargs):
        response = self.client.put(self.base_url + url, data=data, **kwargs)
        return response
   
    def delete(self, url, **kwargs):
        response = self.client.delete(self.base_url + url, **kwargs)
        return response
   
    def options(self, url, **kwargs):
        response = self.client.options(self.base_url + url, **kwargs)
        return response
   
    def request(self, method, url, **kwargs):
        response = self.client.request(method, self.base_url + url, **kwargs)
        return response


