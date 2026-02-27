from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.employees.models.employee import Employee
from apps.employees.selectors.employee_selector import get_all_employees
from apps.employees.serializers.employee_serializer import EmployeeSerializer
from apps.employees.services.employee_service import create_employee, delete_employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        employees = get_all_employees()
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            employee = create_employee(request.data)
            serializer = self.get_serializer(employee)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        employee_id = kwargs.get(self.lookup_field)
        try:
            delete_employee(employee_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

