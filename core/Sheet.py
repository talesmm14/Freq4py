import docx
from calendar import month, monthrange, weekday
import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


class Sheet():
    def __init__(self, path, save_path, year, month):
        self.doc = docx.Document(path)
        self.path = path
        self.save_path = save_path
        self.year = year
        self.month = month
        self.month_days = monthrange(year, month)[1]
        self.year_month_title = (datetime.date(
            year, month, 1).strftime('%B')).swapcase() + "/" + str(year)
        self.key_table = {
            "AS": "",
            "HM1": "08:00",
            "HM2": "14:00",
            "HV1": "12:00",
            "HV2": "18:00",
        }

    def replace_keys(self, key_words):
        for variable_key, variable_value in key_words.items():
            for paragraph in self.doc.paragraphs:
                self.replace_text_in_paragraph(
                    paragraph, variable_key, variable_value)

            for table in self.doc.tables:
                for col in table.columns:
                    for cell in col.cells:
                        for paragraph in cell.paragraphs:
                            self.replace_text_in_paragraph(
                                paragraph, variable_key, variable_value)

    def replace_text_in_paragraph(paragraph, key, value):
        if key in paragraph.text:
            inline = paragraph.runs
            for item in inline:
                if key in item.text:
                    item.text = item.text.replace(key, value)

    def replace_table_values(self):
        day = 0
        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if cell.text == "HM1":
                        for paragraph in cell.paragraphs:
                            day += 1
                            if day <= self.month_days:
                                weekday = date(
                                    year=self.year, month=self.month, day=day).weekday()
                            paragraph.text = self.key_table["HM1"]

                    if cell.text == "AM1":
                        for paragraph in cell.paragraphs:
                            replace_text_in_paragraph_in_table(
                                paragraph, "AS", weekday)

                    if cell.text == "HM2":
                        for paragraph in cell.paragraphs:
                            paragraph.text = self.key_table["HM2"]

                    if cell.text == "AM2":
                        for paragraph in cell.paragraphs:
                            replace_text_in_paragraph_in_table(
                                paragraph, "AS", weekday)

                    if cell.text == "HV1":
                        for paragraph in cell.paragraphs:
                            paragraph.text = self.key_table["HV1"]

                    if cell.text == "AV1":
                        for paragraph in cell.paragraphs:
                            replace_text_in_paragraph_in_table(
                                paragraph, "AS", weekday)

                    if cell.text == "HV2":
                        for paragraph in cell.paragraphs:
                            paragraph.text = self.key_table["HV2"]

                    if cell.text == "AV2":
                        for paragraph in cell.paragraphs:
                            replace_text_in_paragraph_in_table(
                                paragraph, "AS", weekday)


    def replace_text_in_paragraph_in_table(self, paragraph, key, weekday):
        if weekday == 5:
            paragraph.text = "SÁBADO"
            return

        if weekday == 6:
            paragraph.text = "DOMINGO"
            return

        paragraph.text = self.key_table[key]

    def save(self, key_words):
        self.replace_keys(self, key_words)
        self.replace_table_values(self)
        self.doc.save(self.save_path + '/Frequência_{}.docx'.format())
