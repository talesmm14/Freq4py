import docx


def main():
    path = '../Freq4py/Frequência - Modelo.docx'

    doc = docx.Document(path)

    key_words = {"${CAMPO_NOME}": "Tales Monteiro Melquiades",
                 "${CAMPO_LOTACAO}": "",
                 "${CAMPO_CARGO}": "",
                 "${CAMPO_CARGO_COMISSIONADO}": "",
                 "${CAMPO_LOTACAO}": "",
                 "${CAMPO_HORARIO}": "",
                 "${CAMPO_MES_ANO}": "",
                 "${CAMPO_CHEFE}": "",
                 "${CAMPO_CHEFE_MEDIATO}": "",
                 }
    

    for variable_key, variable_value in key_words.items():
        for paragraph in doc.paragraphs:
            print(paragraph.text, variable_key, variable_value)
            replace_text_in_paragraph(paragraph, variable_key, variable_value)

        for table in doc.tables:
            for col in table.columns:
                for cell in col.cells:
                    for paragraph in cell.paragraphs:
                        replace_text_in_paragraph(paragraph, variable_key, variable_value)



    doc.save('../Freq4py/save_doc/Frequência_{}.docx'.format(key_words['${CAMPO_NOME}']))


def replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)


if __name__ == '__main__':
    main()
