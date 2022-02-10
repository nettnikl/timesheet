from openpyxl import Workbook, load_workbook, drawing
import datetime
import PIL.Image

workbook = load_workbook("template.xlsx")
worksheet = workbook.active

offset = 9
first_day = datetime.date.today().replace(day=1)
for row in range(24):
    d = first_day + datetime.timedelta(days=row)
    worksheet.cell(row=row+offset, column=1, value=d.strftime("%a, %d.%m.%Y"))
    worksheet.cell(row=row+offset, column=3, value=f"10:00:00")
    worksheet.cell(row=row+offset, column=4, value=f"14:30:00")
    worksheet.cell(row=row+offset, column=5, value=f"00:30:00")

fp = open("sign.png", "rb")
img = PIL.Image.open(fp)

worksheet.cell(row=36, column=5, value=f"Musterstadt, 01.02.2022")

width = 205
wpercent = (width/float(img.size[0]))
height = int(float(img.size[1])*float(wpercent))

resizedImg = img.resize((width, height), PIL.Image.ANTIALIAS)
fp.seek(0)
resizedImg.fp = fp

table_img = drawing.image.Image(resizedImg)
table_img.anchor = "E37"
worksheet.add_image(table_img)

worksheet.protection.enable()

workbook.save("test_out.xlsx")
