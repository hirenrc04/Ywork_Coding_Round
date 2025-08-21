from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    leave_count = models.PositiveIntegerField(default=30)

    def calculate_payable_salary(self):
        return self.base_salary

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    leave_count = models.IntegerField(default=0)
    month = models.IntegerField(null=True, blank=True)  # Add this
    year = models.IntegerField(null=True, blank=True)   # Add this

    def __str__(self):
        return f"Leave Application by {self.employee} from {self.start_date} to {self.end_date}"