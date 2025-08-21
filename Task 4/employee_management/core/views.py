from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Department, LeaveApplication
from .serializers import EmployeeSerializer, DepartmentSerializer, LeaveApplicationSerializer
from rest_framework import generics
from django.db.models import F
from rest_framework.views import APIView
from django.db.models.functions import ExtractMonth, ExtractYear

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

    def update_leave_count(self, request, pk=None):
        leave_application = self.get_object()
        leave_application.leave_count -= 1
        leave_application.save()
        return Response({'status': 'leave count updated'})

class HighEarnersViewSet(viewsets.ViewSet):
    def list(self, request):
        high_earners = Employee.objects.filter(salary__gt=100000)  # Example threshold
        serializer = EmployeeSerializer(high_earners, many=True)
        return Response(serializer.data)

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class LeaveApplicationListCreateView(generics.ListCreateAPIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

class HighEarnersListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        if department_id:
            qs = Employee.objects.filter(department_id=department_id)
            top_salaries = (
                qs.order_by('-base_salary')
                .values_list('base_salary', flat=True)
                .distinct()[:3]
            )
            return qs.filter(base_salary__in=top_salaries)
        return Employee.objects.none()

class LeaveApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

class CalculatePayableSalaryView(APIView):
    def post(self, request):
        employee_id = request.data.get('employee_id')
        month = request.data.get('month')
        year = request.data.get('year')
        try:
            employee = Employee.objects.get(pk=employee_id)
            leave = LeaveApplication.objects.annotate(
                leave_month=ExtractMonth('start_date'),
                leave_year=ExtractYear('start_date')
            ).filter(
                employee=employee,
                leave_month=month,
                leave_year=year
            ).first()
            leave_count = leave.leave_count if leave else 0
            payable_salary = employee.base_salary - (leave_count * (employee.base_salary / 25))
            return Response({'payable_salary': payable_salary})
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=404)

class HighEarnersMonthListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        if department_id and month and year:
            # Find employees in department
            qs = Employee.objects.filter(department_id=department_id)
            # Find top 3 unique base salaries for that department in that month
            top_salaries = (
                qs.order_by('-base_salary')
                .values_list('base_salary', flat=True)
                .distinct()[:3]
            )
            # Filter employees who have leave applications in that month/year and are high earners
            return qs.filter(
                base_salary__in=top_salaries,
                leaveapplication__start_date__month=month,
                leaveapplication__start_date__year=year
            ).distinct()
        return Employee.objects.none()