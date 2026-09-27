from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from visitors.models import VisitorRequest

@login_required
def home(request):
    if request.user.is_staff or request.user.is_superuser:
        return render(request,'dashboard/staff.html',{
            'pending':VisitorRequest.objects.filter(status='Pending').count(),
            'approved':VisitorRequest.objects.filter(status='Approved').count(),
            'inside':VisitorRequest.objects.filter(status='Inside').count(),
        })
    student=getattr(request.user,'student_profile',None)
    return render(request,'dashboard/student.html',{'student':student,'requests':VisitorRequest.objects.filter(student=student) if student else []})
