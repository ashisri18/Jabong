import xlrd
import sys, traceback

class ExcelSheet():

    def __init__(self):
        # self.rowNum = rowNum
        # self.colNum = colNum
        # self.sheetName = sheetName
        self.excelPath = "E:\Automation\BackUp\Git\Jabong\TestData.xlsx"

    def readExcelData(self,sheetName, rowNum, colNum):
        workbook = xlrd.open_workbook(self.excelPath)
        worksheet = workbook.sheet_by_name(sheetName)
#       for current_Row in range(worksheet.nrows):
        cellValue = worksheet.cell_value(rowNum, colNum)
        return cellValue

    def readData(self,testCaseId,sheetName):
            data = []
    #    try:
            workbook = xlrd.open_workbook("D:\CBT_Automation\Python\Workspace_Python\Jabong\TestData.xlsx")
            worksheet = workbook.sheet_by_name(sheetName)
            # print (worksheet)
            for current_Row in range(worksheet.nrows):
                # print(worksheet.row(current_Row)[0])
                print(testCaseId)
                current_Id = str(worksheet.row(current_Row)[0])[6:15]

                print(current_Id)
                if current_Id == testCaseId:
                    print("Inside If loop.")
                    # print(worksheet.row(current_Row)[0])
                    for current_cell in range(worksheet.ncols):
                        print(worksheet.ncols)
                        print(current_cell)
                        #print(data)
                        data.append(worksheet.cell_value(current_Row, current_cell))
                        print(data)
                    print("out of For 2 loop.")
                    break
                print("out of if loop.")
            print("out of For 1 loop.")
            print(data)
            return data

        #except:
            traceback.print_exception("there is some exception.")




