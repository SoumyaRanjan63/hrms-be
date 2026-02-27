from rest_framework import serializers

from apps.employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "employee_id",
            "full_name",
            "email",
            "department",
            "created_at",
        ]

