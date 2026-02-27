from django.db.models import QuerySet

from apps.attendance.models import Attendance


def get_attendance_by_employee(employee_id: int) -> QuerySet[Attendance]:
    return (
        Attendance.objects.select_related("employee")
        .filter(employee_id=employee_id)
        .order_by("-date")
    )


def get_all_attendance() -> QuerySet[Attendance]:
    return Attendance.objects.select_related("employee").order_by("-date")
