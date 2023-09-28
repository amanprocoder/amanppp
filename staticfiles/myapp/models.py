from django.db import models



class EmployeeDetails(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    department = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    image = models.ImageField(upload_to='employee_images/')

class AttendanceDetail(models.Model):
    employee = models.CharField(max_length=100)
    attendance = models.CharField(max_length=100)
    date = models.DateField()

class managerDetails(models.Model):
    managername = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

class LeaveRequest(models.Model):
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    reason = models.TextField()


