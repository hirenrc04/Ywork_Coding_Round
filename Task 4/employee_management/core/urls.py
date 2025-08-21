from django.urls import path
from core import views
from core.views import CalculatePayableSalaryView, HighEarnersMonthListView

urlpatterns = [
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('leave-applications/', views.LeaveApplicationListCreateView.as_view(), name='leave-application-list-create'),
    path('leave-applications/<int:pk>/', views.LeaveApplicationDetailView.as_view(), name='leave-application-detail'),  # <-- Add this line
    path('salaries/high-earners/', views.HighEarnersListView.as_view(), name='high-earners'),
    path('salaries/high-earners-month/', HighEarnersMonthListView.as_view(), name='high-earners-month'),
    path('calculate-payable-salary/', CalculatePayableSalaryView.as_view(), name='calculate-payable-salary'),
]