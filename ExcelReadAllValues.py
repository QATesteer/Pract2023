import openpyxl
import ExcelOperationBasics

# path = "C:/Users/Dell/Desktop/DDT.xlsx"
workbook = openpyxl.load_workbook("C:/Users/Dell/Desktop/DDT.xlsx")

sh = workbook["DDT"]

rows = ExcelOperationBasics.getRowCount(workbook,'DDT')
# columns = ExcelOperationBasics.getColumnCount(path,'DDT')

# read = ExcelOperationBasics.readData(workbook, 'Sheet1',9,9)

# for r in range(1,rows+1):
#     for c in range(1,columns+1):
#         d = sh.cell(r,c)
#         print(d.value)

# print(sh['A1'].value)