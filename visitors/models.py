from django.db import models
from accounts.models import Student

class Visitor(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField(blank=True)
    id_proof=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class VisitorRequest(models.Model):
    STATUS=[('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected'),('Inside','Inside'),('Completed','Completed')]
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='visitor_requests')
    visitor=models.ForeignKey(Visitor,on_delete=models.CASCADE,related_name='requests')
    purpose=models.TextField()
    visit_date=models.DateField()
    status=models.CharField(max_length=20,choices=STATUS,default='Pending')
    entry_time=models.DateTimeField(null=True,blank=True)
    exit_time=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['-created_at']
    def __str__(self): return f"{self.visitor.name} -> {self.student.student_id}"
