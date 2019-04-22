# coding:utf-8
import json

# 在vscode中相对路径要以当前文件上所在文件夹开始？
# fp = open("web/demofile/json_file.json")
# data = json.load(fp)

class OperationJson():
    # 每次进来都要调用，不如直接初始化的时候就拿到这个data数据
    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open('../data/json_file.json') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self,id=None):
        return self.data[id]

if __name__ == '__main__':
    opjson = OperationJson()

    print(opjson.get_data('addcart'))
    print(type(opjson.get_data('addcart')))
