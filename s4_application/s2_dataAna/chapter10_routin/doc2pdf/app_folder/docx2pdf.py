# -*- coding:utf-8 -*-
__author__ = 'young'
# https://blog.csdn.net/san1156/article/details/77885995
from win32com.client import Dispatch, constants, gencache
import os


def transfer_doc2pdf():
    input_filepath = input('')
    output = input('')
    w = Dispatch("Word.Application")
    try:
        doc = w.Documents.open(input, ReadOnly=1)
        doc.ExportAsFixFormat(output,
                              constants.wdExportFormatPDF,
                              Item=constants.wdExportDocumentWithMarkup,
                              CreateBookmarks=constants.wdExportCreateHeadingBookmarks,
                              )
    except:
        pass
    finally:
        w.Quit(constants.wdDoNotSaveChanges)
    if os.path.isfile(output):
        print('')
    else:
        print('')
