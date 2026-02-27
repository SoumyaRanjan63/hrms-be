from typing import Optional

from apps.employees.models.employee import Employee


def get_all_employees():
    return Employee.objects.order_by("-created_at")


def get_employee_by_id(employee_id: int) -> Optional[Employee]:
    try:
        return Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return None
