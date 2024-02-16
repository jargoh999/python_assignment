class Person:
    countNumberOfProblems = 0
    problems = []
    problems_and_counter = {}

    def add_problems(self, problem, numberOfProblem=None):
        if numberOfProblem is None:
            self.problems.append(problem)
            problem.isSolved = False
        else:
            self.countNumberOfProblems += 1
            self.problems_and_counter[problem.getDescription()] = self.countNumberOfProblems

    def remove_problem(self, problem):
        self.problems.remove(problem)
        problem.isSolved = True

    def count_problem(self):
        return self.problems

    def getProblem_size(self) -> int:
        return len(self.problems)
