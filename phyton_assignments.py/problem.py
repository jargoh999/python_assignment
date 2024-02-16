import type_of_problems


class Problem(object):
    description = str()
    typeOfProblem = type_of_problems.TypeOfProblems
    isSolved = bool()

    def __init__(self, description, typeOfProblem):
        self.description = description
        self.typeOfProblem = typeOfProblem

    def getDescription(self):
        return self.description

    def __str__(self):
        return f"{self.getDescription()}"
