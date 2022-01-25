# -*- coding: utf-8 -*-
'''
@File  : Request.py
@Date  : 2020/4/3 10:40
@Author: 
@Desc  : 
'''

"""
封装request
"""

import os
import random
import requests

from requests_toolbelt import MultipartEncoder
from base import consts



class Request:

    def __init__(self):
        pass


    def run_request(self,method,*args,**kwargs):
        if method == 'post':
            res = self.post_request(*args,**kwargs)
        elif method == 'get':
            res = self.get_request(*args,**kwargs)
        elif method == 'put':
            res = self.put_request(*args,**kwargs)
        elif method == 'patch':
            res = self.put_request(*args,**kwargs)
        elif method == 'delete':
            res = self.delete_request(*args,**kwargs)
        elif method == 'post_multipart':
            res = self.post_request_multipart(*args,**kwargs)
        else:
            res='请求方法错误，请检查'
        return res


    def get_request(self, url, data, header=None):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        try:
            if data is None:
                response = requests.get(url=url, headers=header)
            else:
                response = requests.get(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        return self.process_response(response)

    def post_request(self, url,data=None, json=None,header=None, **kwargs):
        """
        Post请求
        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """

        try:
            response = requests.post(url=url, data=data, json=json, headers=header, verify=False)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        return self.process_response(response)

    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        return self.process_response(response)

    def put_request(self, url,json=None,data=None, header=None):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:
        """

        try:
            response = requests.put(url=url, json=json,data=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()


        return self.process_response(response)

    def patch_request(self, url,json=None,data=None, header=None):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:
        """

        try:
            response = requests.patch(url=url, json=json,data=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()


        return self.process_response(response)

    def delete_request(self, url,json=None,data=None, header=None):
        """
        delete请求
        :param url:
        :param data:
        :param header:
        :return:
        """

        try:
            response = requests.delete(url=url, json=json,data=data ,headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()


        return self.process_response(response)

    def process_response(self,response):
        """

        :param response:
        :return: {"code":"","body":"","text","time_consuming":"","time_total":""}
        """
        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        consts.TIMES_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
