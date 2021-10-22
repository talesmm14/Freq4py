from core.Commissioned import Commissioned
from core.Sheet import Sheet
from core.Trainee import Trainee

def main():

    not_working_days = {
        1: "RECESSO",
        15: "FERIADO",
        17: "FALTA",
    }


    estagiario = Trainee("TALES MONTEIRO MELQUIADES", "STEFAN QUEIROZ BARBOSA", "112357005-1").key_words()

    normal = Commissioned(
        "TALES MONTEIRO MELQUIADES",
        "LOTAÇÃO DE TESTE",
        "MANDA CHUVA",
        "CHEFÃO",
        "12383434-8",
        "JOÃO DA SILA",
        "ALINO MOURA"
    ).key_words()

    sheet = Sheet(
        "../Freq4py/Frequência - Modelo.docx",
        "../Freq4py/save_doc",
        2021,
        12,
        normal,
        not_working_days
    )

    sheet.save()

if __name__ == '__main__':
    main()