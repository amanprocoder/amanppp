from django.shortcuts import render
import random
import string
from django.core.mail import send_mail

from django.http import HttpResponseRedirect,HttpResponse
from .models import EmployeeDetails,AttendanceDetail,LeaveRequest,managerDetails
from datetime import datetime


def home(request):
    # Redirect to a specific URL
    return render(request,'index.html')

def elogin(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        passw = request.POST.get('password')

        record = EmployeeDetails.objects.get(name=name)
        password=record.password
        image=record.image
        print(password)
        print(passw)
        if passw==password:
            return render(request,'employeemain.html', {'record': record})
        else:
            return HttpResponse('error')

     else:
            
         pass         
         
     return render(request,'elogin.html')

def registration(request):
  
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        department = request.POST.get('department')
        mobile_number = request.POST.get('mobile_number')
        image = request.FILES['imageab']

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
        print(password)


        # Create a new EmployeeDetails instance
        user=EmployeeDetails.objects.create(
            name=name,
            dob=dob,
            email=email,
            department=department,
            mobile_number=mobile_number,
            password=password,
            image=image,
        )
        user.save()

        subject = 'Your Password'
        message = f'Your password is: {password}'
        from_email = 'amanpathak62788@gmail.com'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a success page or perform further actions
        return HttpResponseRedirect('/elogin/')

    return render(request, 'registratio.html')

def employeemain(request):

    pass



def mark_attendance(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        
        date_time = datetime.now()  # Capture the current date and time
        is_present = request.POST.get('status')
        print(f"Status: {is_present}")
        
        AttendanceDetail.objects.create(employee=name, date=date_time, attendance=is_present)
        message='successful'
        
        return HttpResponse('your attendence  saved')
    return render(request, 'attendance_app/mark_attendance.html')

def showattendence(request):

        if request.method == 'POST':
            employee_name = request.POST.get('name')
            attendances = AttendanceDetail.objects.filter(employee=employee_name)
            return render(request, 'showattendence.html', {'attendances': attendances})
        return render(request, 'showattendence.html')

def leave(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        reason = request.POST.get('reason')
        LeaveRequest.objects.create(employee_name=name,email=email,reason=reason)

        request.session['name'] = name
        request.session['email'] = email
        request.session['reason'] = reason
     return HttpResponse('the leave request is goe to your manager the reply will come in your email')


def manager(request):
   

    name = request.session.get('name')
    email = request.session.get('email')
    reason = request.session.get('reason')
    messagea="please give reply to live"
    if request.method == 'POST':
        value = request.POST.get('acceptance')
        if value!=None:
            subject="reply to live application "
            
            message = f'Your leave application is: {value} by manager'
            from_email = 'amanpathak62788@gmail.com'
            recipient_list = [email]
            messagea="reply goest to user email"

            send_mail(subject, message, from_email, recipient_list)
        else:
            return HttpResponseRedirect('/manager/')
           
    return render(request,"manager.html",{'name':name,'email':email,'reason':reason,'messagea':messagea })

def all(request):
    


    employee_data = EmployeeDetails.objects.all()
    return render(request, 'all.html', {'employee_data': employee_data})


  

def attendance_details(request):
    attendance_data = AttendanceDetail.objects.all()
    return render(request, 'attendance_details.html', {'attendance_data': attendance_data})
def mlogin(request):
      
      if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('password')



        record = managerDetails.objects.get(managername=uname)
        password=record.password
        print(password)
        print(passw)
        if passw==password:
            return HttpResponseRedirect('/manager/')


        else:
            return HttpResponse('error')
      else:
          pass
      return render(request, 'mlogin.html')





      
      
     
      


        
        

    


     


    










