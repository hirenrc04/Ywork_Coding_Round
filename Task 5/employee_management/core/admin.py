from django.contrib import admin
from .models import Employee, Department, LeaveApplication

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(LeaveApplication)