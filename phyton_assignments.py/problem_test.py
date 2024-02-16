import unittest
import problem
import type_of_problems
import person


class MyTestCase(unittest.TestCase):

    def test_that_problem_exist(self):
        problem1 = problem.Problem("money", type_of_problems.TypeOfProblems.EDUCATION)
        problem2 = problem.Problem("CAR", type_of_problems.TypeOfProblems.BUSINESS)
        person1 = person.Person()
        person1.add_problems(problem)
        person1.add_problems(problem1)
        self.assertEqual(2, person1.getProblem_size())


class TestMyProblemMethod(unittest.TestCase):

    def test_that_problem_can_be_removed(self):
        problem2 = problem.Problem("GOLD", type_of_problems.TypeOfProblems.EDUCATION)
        problem1 = problem.Problem("CAR", type_of_problems.TypeOfProblems.BUSINESS)
        person2 = person.Person()
        person2.add_problems(problem1)
        person2.add_problems(problem2)
        person2.remove_problem(problem1)
        person2.add_problems(problem1, 1)
        person2.add_problems(problem2, 3)
        print(person2.count_problem())
        print(person2.problems)
        self.assertTrue(problem1.isSolved)
        self.assertFalse(problem2.isSolved)

    def test_that_problem_can_be_unsolved__when_added(self):
        problem1 = problem.Problem("CAR", type_of_problems.TypeOfProblems.BUSINESS)
        person3 = person.Person()
        person3.add_problems(problem1)
        self.assertFalse(problem1.isSolved)
