from apps.employees.models.employee import Employee
from apps.employees.serializers.employee_serializer import EmployeeSerializer


def create_employee(data: dict) -> Employee:
    serializer = EmployeeSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    employee = serializer.save()
    return employee


def delete_employee(employee: Employee) -> None:
    if not employee:
        raise ValueError("Employee not found")

    employee.is_active = False
    employee.save(update_fields=["is_active"])
