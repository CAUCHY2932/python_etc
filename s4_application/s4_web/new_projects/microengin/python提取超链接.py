# coding:utf-8
import xlrd 
"""


假如xlsx较复杂，夹杂着各种格式、规则、宏，可能就会遇到问题---普通读取会丢掉所有这些附带的信息。
其实xlrd早就已经适配了这个功能，
它提供的formatting_info参数取值为True时（为了节省内存，该参数默认为False），就会读取各种格式的信息。

但是对于
xlsx文件会出现以下问题
NotImplementedError: formatting_info=True not yet implemented
这是因为我们设置formatting_info=True，想要读取全部信息
可以采用以下方式

修改为xlsx为xls（推荐）

将xlsx另存为xls，然后再进行后续操作，亲测有效，能正常保存Excel原有格式， 不用修改代码。


使用pywin32

这是用于Win32 (pywin32)扩展的Python扩展库，它提供了对许多来自Python的Windows api的访问。


"""
#使用pywin32


def get_link(col_index, row_start, row_end, file_name):
    main_data_book = xlrd.open_workbook(file_name, formatting_info=True) 
    main_data_sheet = main_data_book.sheet_by_index(0) 
    for row in range(row_start, row_end):  
        link = main_data_sheet.hyperlink_map.get((row, col_index))#row和col分别为要提取超链接信息的单元格行和列
        url=link.url_or_path
        print(url)


def get_link_ver_2():
    main_data_book = xlrd.open_workbook("IEsummary.xls", formatting_info=True)
    main_data_sheet = main_data_book.sheet_by_index(0)
    for row in range(1, 101):
        row_values = main_data_sheet.row_values(row, start_colx=0, end_colx=8)
        company_name = row_values[0]

        link = main_data_sheet.hyperlink_map.get((row, 0))
        url = '(No URL)' if link is None else link.url_or_path
        print(company_name.ljust(20) + ': ' + url)


def get_link_mine(col_index, row_start, row_end, file_name):
    main_data_book = xlrd.open_workbook(file_name, formatting_info=True) 
    main_data_sheet = main_data_book.sheet_by_index(0) 
    for row in range(row_start, row_end):  
        link = main_data_sheet.hyperlink_map.get((row, col_index))#row和col分别为要提取超链接信息的单元格行和列
        url = '(No URL)' if link is None else link.url_or_path
        print(url)


if __name__ == "__main__":
    get_link_mine(1, 1, 12, './test_link.xls')
