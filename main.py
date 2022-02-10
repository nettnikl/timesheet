from openpyxl import Workbook, load_workbook, drawing

workbook = load_workbook("template.xlsx")
worksheet = workbook.active

for row in range(1, 10):
    worksheet.cell(row=row, column=1, value=f'NEW VALUE {row}')

img = drawing.image.Image('sign.png')
img.anchor = 'F37'
worksheet.add_image(img)

worksheet.protection.enable()

workbook.save("test_out.xlsx")
