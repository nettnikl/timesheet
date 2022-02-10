from openpyxl import Workbook, load_workbook, drawing

workbook = load_workbook("template.xlsx")
worksheet = workbook.active

for row in range(24):
    worksheet.cell(row=row+9, column=1, value=f'NEW VALUE {row}')
    worksheet.cell(row=row+9, column=3, value=f'10:00:00')
    worksheet.cell(row=row+9, column=4, value=f'14:30:00')
    worksheet.cell(row=row+9, column=5, value=f'00:30:00')

img = drawing.image.Image('sign.png')
img.anchor = 'E38'
worksheet.add_image(img)

worksheet.protection.enable()

workbook.save("test_out.xlsx")
