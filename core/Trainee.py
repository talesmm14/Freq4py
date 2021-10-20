class Trainee():
    def __init__(self, name, supervisor, supervisor_registration, schedule):
        self.name = name
        self.supervisor = supervisor
        self.supervisor_registration = supervisor_registration
        self.schedule = schedule

    def get_key_words(self):
        return {
        "${FIELD_DATE}": "",
        "${FIELD_TITLE_1}": "NOME:",
        "${FIELD_TITLE_2}":  "SUPERVISOR:",
        "${FIELD_TITLE_3}":  "CARGO:",
        "${FIELD_TITLE_4}":  "",
        "${FIELD_TITLE_5}":  "",
        "${FIELD_TITLE_6}":  "HORÁRIO:",
        "${FIELD_TITLE_7}":  "Assinatura Supervisor(A):",
        "${FIELD_TITLE_8}":  "",

        "${FIELD_VALUE_1}": self.name,
        "${FIELD_VALUE_2}": self.supervisor,
        "${FIELD_VALUE_3}": "Estagiario",
        "${FIELD_VALUE_4}": "",
        "${FIELD_VALUE_5}": "",
        "${FIELD_VALUE_6}": self.schedule,
        "${FIELD_VALUE_7}": "",
        "${FIELD_VALUE_8}": "",
    }
    