from django import forms
from .models import Visitor,VisitorRequest
class VisitorForm(forms.ModelForm):
    class Meta:
        model=Visitor
        fields=['name','phone','email','id_proof']
        widgets={x:forms.TextInput(attrs={'class':'form-control'}) for x in ['name','phone','email','id_proof']}
class VisitorRequestForm(forms.ModelForm):
    class Meta:
        model=VisitorRequest
        fields=['purpose','visit_date']
        widgets={'purpose':forms.Textarea(attrs={'class':'form-control','rows':3}),'visit_date':forms.DateInput(attrs={'class':'form-control','type':'date'})}
