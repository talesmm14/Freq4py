from core.Commissioned import Commissioned
from core.Sheet import Sheet
from core.Trainee import Trainee

def main():
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
        10,
        estagiario
    )

    sheet.save()

if __name__ == '__main__':
    main()