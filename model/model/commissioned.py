
class Commissioned():
    def __init__(self, name, capacity, effective_position, commissioned_position, registration, immediate_boss, mediate_boss):
        self.name = name
        self.capacity = capacity
        self.effective_position = effective_position
        self.commissioned_position = commissioned_position
        self.registration = registration
        self.immediate_boss = immediate_boss
        self.mediate_boss = mediate_boss

    def key_words(self):
        return {
            "${FIELD_DATE}": "",
            "${FIELD_TITLE_1}": "NOME:",
            "${FIELD_TITLE_2}": "LOTAÇÃO:",
            "${FIELD_TITLE_3}": "CARGO EFETIVO:",
            "${FIELD_TITLE_4}": "CARGO COMISSIONADO:",
            "${FIELD_TITLE_5}": "MATRÍCULA:",
            "${FIELD_TITLE_7}": "Chefe Imediato:",
            "${FIELD_TITLE_8}": "Chefe Mediato:",

            "${FIELD_VALUE_1}": self.name,
            "${FIELD_VALUE_2}": self.capacity,
            "${FIELD_VALUE_3}": self.effective_position,
            "${FIELD_VALUE_4}": self.commissioned_position,
            "${FIELD_VALUE_5}": self.registration,
            "${FIELD_VALUE_7}": self.immediate_boss,
            "${FIELD_VALUE_8}": self.mediate_boss,
        }
