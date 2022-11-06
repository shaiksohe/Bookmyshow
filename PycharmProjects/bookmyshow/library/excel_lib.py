import re
import pytest
import datetime
import xlrd
from library.config import Config
from selenium import webdriver


class ReadExcel:

    def read_testdata(self,sheetname):
        wb = xlrd.open_workbook(Config. LOCATORS )
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []
        for row in rows:
            if columns == 1:
                data.append(row[0].value)
            else:
                values = ()
                for j in range(columns):
                    values += (row[j].value,)
                data.append(values)
        return data

    def read_locators(self, sheetname):
        # f_path = r"C:\Users\91779\Desktop\reg_locators.xlsx"
        wb = xlrd.open_workbook(Config.LOCATORS)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        d1 = {}
        for row in rows:
            d1[row[0].value] = (row[1].value, row[2].value)

        return d1


n = ReadExcel()
h = n.read_locators("activities")
#
print(h)
