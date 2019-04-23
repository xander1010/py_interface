#coding:utf-8
import requests

class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)  #如果返回的本身就是json,就不用加.json()转换
        else:
            res = requests.post(url=url,data=data)   #如果返回的本身就是json,就不用加.json()转换
        return res.json()

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header)   #如果返回的本身就是json,就不用加.json()转换
        else:
            res = requests.get(url=url,data=data)  #如果返回的本身就是json,就不用加.json()转换
        return res.text


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res


if __name__ == '__main__':
    run = RunMethod()
    url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
    # print(run.run_main('get',url))


    header = {
        "token":"d8f5d03665d32c572834010682c2a88c",
        "cid":"lianfeng",
        "Content-Type":"application/json",
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
    }
    url1 = 'http://dev.api.tianbaows.com/lianfeng/search'

    data = {
          "cid":"lianfeng",
          "adultNumber":"1",
          "itineraries":[{
            "departureCode":"YTO",
            "arrivalCode":"NYC",
            "departureDate":"20190625"
            }]
        }
    print(run.run_main('post',url1,data,header))

    print(requests.post(url1,data=data,headers=header).json())
