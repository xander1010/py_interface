import xlrd
import os,sys

class OperationExcel:
    def __init__(self,file_neme=None,sheet_id=None):
        if file_neme:
            # path = os.path.dirname(__file__)
            self.file_neme = '../data/'+ file_neme
            self.sheet_id = sheet_id
        else:
            # 获取当前文件所在路径
            # path = os.path.dirname(__file__)
            # self.file_neme = path + '/Newfile.xls'
            self.file_neme = '../data/interface.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_neme)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取sheet行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

if __name__ == '__main__':
    opers = OperationExcel()
    # print(opers.get_data().nrows)

    print(opers.get_lines())
    print(opers.get_cell_value(1,1))
    
    # 获取指定路径或文件的绝对路径
    print(os.path.abspath('interface.xlsx'))

