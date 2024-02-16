from enum import Enum


class TypeOfProblems(Enum):
    FINANCIAL = "financial"
    SPIRITUAL = "spiritual"
    EDUCATION = "education"
    BUSINESS = "business"
    TECHNICAL = "technical"

    def getValue(self):
        return self.value
