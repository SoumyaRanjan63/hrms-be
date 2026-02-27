from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.attendance.models import Attendance
from apps.attendance.selectors.attendance_selector import get_attendance_by_employee, get_all_attendance
from apps.attendance.serializers.attendance_serializer import AttendanceSerializer
from apps.attendance.services.attendance_service import create_attendance, delete_attendance


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def list(self, request, *args, **kwargs):
        employee_id = request.query_params.get("employee_id")
        if employee_id is not None:
            attendances = get_attendance_by_employee(employee_id=employee_id)
        else:
            attendances = get_all_attendance()
        serializer = self.get_serializer(attendances, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            attendance = create_attendance(request.data)
            serializer = self.get_serializer(attendance)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        attendance_id = kwargs.get(self.lookup_field)
        try:
            delete_attendance(attendance_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

