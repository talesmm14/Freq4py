
class Trainee():
    def __init__(self, name, supervisor, supervisor_registration):
        self.name = name
        self.supervisor = supervisor
        self.supervisor_registration = supervisor_registration

    def key_words(self):
        return {
        "${FIELD_DATE}": "",
        "${FIELD_TITLE_1}": "NOME:",
        "${FIELD_TITLE_2}":  "SUPERVISOR(A):",
        "${FIELD_TITLE_3}":  "CARGO:",
        "${FIELD_TITLE_4}":  "SUPERVISOR(A) MATRICULA:",
        "${FIELD_TITLE_5}":  "",
        "${FIELD_TITLE_7}":  "ASSINATURA SUPERVISOR(A):",
        "${FIELD_TITLE_8}":  "",

        "${FIELD_VALUE_1}": self.name,
        "${FIELD_VALUE_2}": self.supervisor,
        "${FIELD_VALUE_3}": "ESTAGIÁRIO",
        "${FIELD_VALUE_4}": self.supervisor_registration,
        "${FIELD_VALUE_5}": "",
        "${FIELD_VALUE_7}": "",
        "${FIELD_VALUE_8}": "",
    }
    