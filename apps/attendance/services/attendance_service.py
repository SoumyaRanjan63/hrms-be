from apps.attendance.models.attendance import Attendance
from apps.attendance.serializers.attendance_serializer import AttendanceSerializer


def create_attendance(data: dict) -> Attendance:
    serializer = AttendanceSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    attendance = serializer.save()
    return attendance


def delete_attendance(attendance_id: int) -> None:
    Attendance.objects.filter(id=attendance_id).delete()

