import pandas as pd
from singleton_for_path import FilePathSingleton
from xlrd import open_workbook


class handleSuffix():
    def __init__(self):
        global file
        file = FilePathSingleton()

    def is_xls(self, file):
        xls_read_file = open_workbook(file.get_file_path())
        sheet = xls_read_file.sheet_by_index(0)
        extracted = []
        for row_idx in range(sheet.nrows):
            extracted.append(sheet.row_values(row_idx))
        xls_to_xlsx = pd.DataFrame(extracted)
        newborn_xlsx_name = file.get_file_name_only() + ".xlsx"
        xls_to_xlsx.to_excel(newborn_xlsx_name, index = False) 
        newborn_xlsx = pd.read_excel(newborn_xlsx_name)
        file.set_file_path(file.get_file_path_only() + newborn_xlsx_name)
    
    def is_xlsx(self, file):
        xlsx_read_file = pd.read_excel(file.get_file_path())
