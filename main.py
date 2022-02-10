from openpyxl import Workbook, load_workbook, drawing
import PIL.Image

workbook = load_workbook("template.xlsx")
worksheet = workbook.active

for row in range(24):
    worksheet.cell(row=row+9, column=1, value=f"NEW VALUE {row}")
    worksheet.cell(row=row+9, column=3, value=f"10:00:00")
    worksheet.cell(row=row+9, column=4, value=f"14:30:00")
    worksheet.cell(row=row+9, column=5, value=f"00:30:00")

fp = open("sign.png", "rb")
img = PIL.Image.open(fp)

width = 240
wpercent = (width/float(img.size[0]))
height = int(float(img.size[1])*float(wpercent))

resizedImg = img.resize((width, height), PIL.Image.ANTIALIAS)
fp.seek(0)
resizedImg.fp = fp

table_img = drawing.image.Image(resizedImg)
table_img.anchor = "E38"
worksheet.add_image(table_img)

worksheet.protection.enable()

workbook.save("test_out.xlsx")
