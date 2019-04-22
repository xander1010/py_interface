#coding:utf-8
import requests
import json


class RunMain:
    
    def __init__(self):
        # url,method,data=None
        # self.res = self.run_main(url,method,data)
        pass

    def send_post(self,url,data):
        res = requests.post(url,data)
        return res.json()

    def send_get(self,url,data):
        res = requests.get(url,data).json()
        # return 
        return res

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
    data = {}
    run = RunMain()
    print(run.run_main(url,'GET'))



