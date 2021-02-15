import openpyxl     #pip install openpyxl==2.6.2

write_wb = openpyxl.Workbook()
write_ws = write_wb.active

write_ws = write_wb.active
write_ws['A1'] = '수량'
write_ws['B1'] = '가격'
write_ws['C1'] = '금액'

write_ws.append([25,5000,125000])
write_ws.append([30,5500,60000])
write_ws.append([35,8000,9000])

for i in range(5):
    write_ws.append([i+1, i+2, i+3])

write_ws.cell(5,5,'셀추가')

write_wb.save('/test.xlsx')

load_wb = openpyxl.load_workbook('./test.xlsx', data_only=True)

load_ws = load_wb['Sheet']

print(load_ws['A1'].value)
