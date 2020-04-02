# encoding: utf-8
'''
@author: lingshu
@file: read_excel.py
@time: 2019/6/21 17:03
@desc: 读取excel
'''
import xlrd
from utils import get_file_path     # 包导入文件


def read_excel():
    # 获取xlsx文件目录
    file_path = get_file_path.get_root_path() + 'testdata\\testdata.xlsx'
    excel_file = xlrd.open_workbook(file_path)

    # 获取sheet内容【1.根据sheet索引 2.根据sheet名称】
    # sheet=ExcelFile.sheet_by_index(1)
    sheet = excel_file.sheet_by_name('Sheet1')
    # 打印sheet的名称，行数，列数
    print(sheet.name)
    print(sheet.nrows)
    print(sheet.ncols)
    """
    python写excel——xlwt
    xlrd.open_workbook(file_path):根据文件路径打开execel文件
        sheet_name_list = excel_file.sheet_names()      excel文件sheet名字
        sheet = excel_file.sheet_by_name()  根据名字获取xecel的sheet的内容
        sheet.name  sheet.nrows     sheet.ncols
        rows = sheet.row_values(3)  获取第三行内容
        cols = sheet.col_values(2)  获取第二列内容
        获取单元格内容
        sheet.cell(1,0).value.encode("utf-8")
        sheet.cell_value(1,0).encode("utf-8")
        sheet.row(1)[0].value.encode("utf-8")
        获取单元格内容的数据类型
        sheet2.cell(1,0).ctype
    """

    # 获取整行或者整列的值
    rows = sheet.row_values(1)
    cols = sheet.col_values(1)
    print(rows)
    print(cols)

    #获取单元格内容
    print("第二行第一列的值为： %s" % sheet.cell(1, 0))

    # 打印单元格内容格式
    print("单元格内容格式为： %s" % sheet.cell(0, 0).ctype)


def get_xls():
    cls = []
    file_path = get_file_path.get_root_path() + 'testdata\\testdata.xlsx'
    # 文件位置
    excel_file = xlrd.open_workbook(file_path)
    sheet = excel_file.sheet_by_name('Sheet1')
    nrows = sheet.nrows
    for i in range(nrows):
        cls.append(sheet.row_values(i))
    return cls
if __name__ == '__main__':
    print(get_xls())