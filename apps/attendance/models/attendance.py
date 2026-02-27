from django.db import models
from apps.employees.models import Employee


class Attendance(models.Model):
    PRESENT = "Present"
    ABSENT = "Absent"

    STATUS_CHOICES = [
        (PRESENT, "Present"),
        (ABSENT, "Absent"),
    ]

    employee = models.ForeignKey(Employee, related_name="attendances", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ["employee", "date"]
