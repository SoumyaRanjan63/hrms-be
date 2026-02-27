from apps.employees.models.employee import Employee
from apps.employees.serializers.employee_serializer import EmployeeSerializer


def create_employee(data: dict) -> Employee:
    serializer = EmployeeSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    employee = serializer.save()
    return employee


def delete_employee(employee_id: int) -> None:
    employee = Employee.objects.filter(id=employee_id).first()
    if not employee:
        raise ValueError("Employee not found")

    if employee.attendances.exists():
        raise ValueError("Cannot delete employee with attendance records")

    employee.delete()
