from django.test import TestCase
from .models import Employee, Department, LeaveApplication

class EmployeeManagementTests(TestCase):

    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.employee = Employee.objects.create(
            name="John Doe",
            department=self.department,
            base_salary=50000,
            leave_count=20
        )

    def test_create_department(self):
        department = Department.objects.create(name="Finance")
        self.assertEqual(department.name, "Finance")

    def test_create_employee(self):
        employee = Employee.objects.create(
            name="Jane Smith",
            department=self.department,
            base_salary=60000,
            leave_count=15
        )
        self.assertEqual(employee.name, "Jane Smith")
        self.assertEqual(employee.department, self.department)

    def test_set_base_salary(self):
        self.employee.base_salary = 55000
        self.employee.save()
        self.assertEqual(self.employee.base_salary, 55000)

    def test_update_leave_count(self):
        self.employee.leave_count -= 1
        self.employee.save()
        self.assertEqual(self.employee.leave_count, 19)

    def test_calculate_payable_salary(self):
        self.assertEqual(self.employee.calculate_payable_salary(), 50000)

    def test_retrieve_high_earners(self):
        high_earners = Employee.objects.filter(base_salary__gt=55000)
        self.assertIn(self.employee, high_earners)  # Assuming employee's salary is not high enough to be included