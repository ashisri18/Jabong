import xlrd
workbook = xlrd.open_workbook('my_file_name.xls')
worksheet = workbook.sheet_by_name('My_Sheet_Name')
sheet.cell(0, 0).value