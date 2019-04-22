# coding:utf-8
import sys
sys.path.append("..")

from util.operation import OperationExcel
from dataconfig import data_config
from util.operation_json import OperationJson

class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # 获取excel行数，就是case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 是否执行
    def get_is_run(self,row):
        flag = None
        col = data_config.get_run()
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'y':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self,row):
        col = data_config.get_header()
        header = self.opera_excel.get_cell_value(row,col)
        if header == 'y':
            return data_config.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_method(self,row):
        col = data_config.get_request_way()
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    # 获取url
    def get_url(self,row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row,col)
        return url

    # 获取请求数据
    def get_request_data(self,row):
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data)
        return request_data

    #获取预期结果
    def get_expcet_data(self,row):
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == '':
            return None
        return expect
