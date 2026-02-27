from rest_framework import serializers

from apps.attendance.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(source="employee.employee_id", read_only=True)
    employee_name = serializers.CharField(source="employee.full_name", read_only=True)

    class Meta:
        model = Attendance
        fields = [
            "id",
            "employee",
            "employee_id",
            "employee_name",
            "date",
            "status",
            "created_at",
        ]

