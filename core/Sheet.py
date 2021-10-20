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
        self.year_month_title = (datetime.date(year, month, 1).strftime('%B')).swapcase() + "/" + str(year)


    def replace_keys(self):
        for variable_key, variable_value in key_words.items():
            for paragraph in self.doc.paragraphs:
                self.replace_text_in_paragraph(paragraph, variable_key, variable_value)

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

    def save(self):
        self.doc.save(self.save_path + '/Frequência_{}.docx'.format()')