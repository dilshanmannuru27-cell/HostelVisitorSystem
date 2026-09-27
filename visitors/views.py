from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Visitor,VisitorRequest
from .forms import VisitorForm,VisitorRequestForm

@login_required
def register_visitor(request):
    student=getattr(request.user,'student_profile',None)
    if not student:
        messages.error(request,'Only students can register visitors.'); return redirect('home')
    vf=VisitorForm(request.POST or None); rf=VisitorRequestForm(request.POST or None)
    if request.method=='POST' and vf.is_valid() and rf.is_valid():
        v=vf.save(); r=rf.save(commit=False); r.student=student; r.visitor=v; r.save()
        messages.success(request,'Visitor request submitted.')
        return redirect('student_visitors')
    return render(request,'visitors/register.html',{'visitor_form':vf,'request_form':rf})

@login_required
def student_visitors(request):
    student=getattr(request.user,'student_profile',None)
    if not student: return redirect('home')
    return render(request,'visitors/student_visitors.html',{'requests':VisitorRequest.objects.filter(student=student)})

def staff(u): return u.is_staff or u.is_superuser

@user_passes_test(staff)
def warden_requests(request):
    return render(request,'visitors/warden.html',{'requests':VisitorRequest.objects.select_related('visitor','student','student__user')})

@user_passes_test(staff)
def update_status(request,pk,status):
    r=get_object_or_404(VisitorRequest,pk=pk)
    if status in ['Approved','Rejected']:
        r.status=status; r.save(); messages.success(request,f'Request {status.lower()}.')
    return redirect('warden_requests')

@user_passes_test(staff)
def security(request):
    qs=VisitorRequest.objects.select_related('visitor','student','student__user')
    return render(request,'visitors/security.html',{'requests':qs.filter(status__in=['Approved','Inside','Completed'])})

@user_passes_test(staff)
def entry(request,pk):
    r=get_object_or_404(VisitorRequest,pk=pk)
    if r.status=='Approved': r.status='Inside'; r.entry_time=timezone.now(); r.save()
    return redirect('security')

@user_passes_test(staff)
def exit(request,pk):
    r=get_object_or_404(VisitorRequest,pk=pk)
    if r.status=='Inside': r.status='Completed'; r.exit_time=timezone.now(); r.save()
    return redirect('security')
