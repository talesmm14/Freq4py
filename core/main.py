from core import Commissioned, Sheet, Trainee


def main():
    sheet = Sheet(
        "../Freq4py/Frequência - Modelo.docx",
        "../Freq4py/save_doc",
        2021,
        10
    )
    
    estagiario = Trainee(

    )

    normal = Commissioned(

    )

    sheet.save(normal.get_key_words())

if __name__ == '__main__':
    main()
