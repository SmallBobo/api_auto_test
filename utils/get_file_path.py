# encoding: utf-8
'''
@author: lingshu
@file: get_file_path.py
@time: 2019/6/21 17:09
@desc: 获取文件路径
'''
import os

project_name = "api_auto_test"
def get_root_path():
    '''
    获取项目根路径
    :param project_name: 项目名
    :return:
    '''
    curPath = os.path.abspath(os.path.dirname(__file__))
    print(curPath)
    '''
    os.path.abspath()   
    返回绝对路径
    print(os.path.abspath("."))   #当前目录的绝对路径
    print(os.path.abspath(r".."))  #上级目录的绝对路径
    print(os.path.abspath(r"D:\python_workshop\python6\revise\函数.py"))
    
    os.path.dirname(__file__)
    两种作用
        1、所在的脚本是以完整的路径运行时，返回完整的路径，例如：python d:/pythonSrc/test/test.py，返回：d:/pythonSrc/test/
        2、所在的脚本是以相对路径运行时，返回空字符串，例如：  python test.py，返回空字符串
    '''
    rootPath = curPath[:curPath.find(project_name+"\\") + len(project_name+"\\")]  # 获取myProject，也就是项目的根路径
    """
    curPath = F:\\pythonprojects\\api_auto_test\\utils
    curPath.find(project_name+"\\") ：返回curPath中api_auto_test的首位置数
    curPath[:curPath.find(project_name+"\\") + len(project_name+"\\")] 
        curPath[startindex:endindex:step]:字符串取值
        curPath[startindex:endindex]:可省略步长
        curPath[startindex:-1]：字符串最后一位为-1，步长为复数为倒叙
    """
    print("rootPath= %s", rootPath)
    return rootPath

if __name__ == '__main__':
    print(get_root_path())