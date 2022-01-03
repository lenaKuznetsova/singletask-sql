
class Enum:
    _mapping = {}

    @classmethod
    def to_string(cls, state_code):
        return cls._mapping[state_code]

    @classmethod
    def from_string(cls, state_name):
        return [i for i in cls._mapping if cls._mapping[i] == state_name][0]
