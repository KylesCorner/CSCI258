# test.py
import unittest
from my_module import max3, odd, majority, Employee, Manager


class TestFunctions(unittest.TestCase):
    def test_max3(self):
        self.assertEqual(max3(1, 2, 3), 3)
        self.assertEqual(max3(10, 5, 7), 10)
        self.assertEqual(max3(-1, -5, -3), -1)

    def test_odd(self):
        self.assertTrue(odd(True, False, False))  # 1 True
        self.assertTrue(odd(True, True, True))  # 3 True
        self.assertFalse(odd(True, True, False))  # 2 True

    def test_majority(self):
        self.assertTrue(majority(True, True, False))
        self.assertTrue(majority(True, True, True))
        self.assertFalse(majority(True, False, False))


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Trish", 100000)

    def test_name(self):
        self.assertEqual(self.emp.name, "Trish")

    def test_salary(self):
        self.assertEqual(self.emp.salary, 100000)

    def test_get_details(self):
        self.assertEqual(self.emp.get_details(), "Name: Trish, Salary: $100000")


class TestManager(unittest.TestCase):
    def setUp(self):
        self.mgr = Manager("Trish", 100000, "Computer Science")

    def test_name(self):
        self.assertEqual(self.mgr.name, "Trish")

    def test_salary(self):
        self.assertEqual(self.mgr.salary, 100000)

    def test_department(self):
        self.assertEqual(self.mgr.department, "Computer Science")

    def test_get_details(self):
        self.assertEqual(
            self.mgr.get_details(),
            "Name: Trish, Salary: $100000, Department: Computer Science",
        )


if __name__ == "__main__":
    unittest.main()
