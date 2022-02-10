from openpyxl import Workbook, load_workbook, drawing
import datetime
import PIL.Image
import locale
import holidays


class TimesheetGenerator:
    def init():
        pass

    def run(self):
        workbook = load_workbook("template.xlsx")
        worksheet = workbook.active

        offset = 9
        locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

        first_day = datetime.date.today().replace(day=1, month=1)
        next_month = first_day.replace(day=28) + datetime.timedelta(days=4)
        last_day = next_month - datetime.timedelta(days=next_month.day)

        holiday_list = holidays.Germany(prov="BY")

        day = first_day
        days = []
        while day <= last_day:
            if day.weekday() in [5, 6]:
                day += datetime.timedelta(days=1)
                continue
            if day in holiday_list:
                days.append((day, holiday_list.get(day)))
                day += datetime.timedelta(days=1)
                continue
            days.append((day, ""))
            day += datetime.timedelta(days=1)

        for row, (day, comment) in enumerate(days):
            worksheet.cell(row=row+offset,
                           column=1,
                           value=day)
            if comment != "":
                worksheet.cell(row=row+offset, column=2, value="Feiertag")
                worksheet.cell(row=row+offset, column=3, value=f"")
                worksheet.cell(row=row+offset, column=4, value=f"")
                worksheet.cell(row=row+offset, column=5, value=f"")
            else:
                worksheet.cell(row=row+offset, column=2, value="")
                worksheet.cell(row=row+offset, column=3,
                               value=datetime.time(10))
                worksheet.cell(row=row+offset, column=4,
                               value=datetime.time(14, 30))
                worksheet.cell(row=row+offset, column=5,
                               value=datetime.time(0, 30))

            day += datetime.timedelta(days=1)

        fp = open("sign.png", "rb")
        img = PIL.Image.open(fp)

        sign_date = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        while sign_date.weekday() in [5, 6]:
            sign_date -= datetime.timedelta(days=1)

        worksheet.cell(row=36,
                       column=5,
                       value=f"Musterstadt, {sign_date.strftime('%a, %d.%m.%Y')}")

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


def main():
    TimesheetGenerator().run()


if __name__ == "__main__":
    main()
