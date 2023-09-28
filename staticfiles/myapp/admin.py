from django.contrib import admin
from .models import EmployeeDetails, AttendanceDetail,managerDetails,LeaveRequest

admin.site.register(EmployeeDetails)
admin.site.register(AttendanceDetail)
admin.site.register(managerDetails)
admin.site.register(LeaveRequest)


