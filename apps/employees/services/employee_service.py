from apps.employees.models.employee import Employee
from apps.employees.serializers.employee_serializer import EmployeeSerializer


def create_employee(data: dict) -> Employee:
    serializer = EmployeeSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    employee = serializer.save()
    return employee


def delete_employee(employee_id: int) -> None:
    Employee.objects.filter(id=employee_id).delete()
