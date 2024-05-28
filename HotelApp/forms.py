from django import forms
from .import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email']
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class Online_Booking_form(forms.ModelForm):
    class Meta:
        model = models.Online_Booking
        fields = "__all__"

class offline_Booking_form(forms.ModelForm):
    class Meta:
        model = models.Offline_Booking
        fields = "__all__"
class Add_Employee_form(forms.ModelForm):
    class Meta:
        model = models.Add_Employee
        fields = "__all__"

class Add_Room_form(forms.ModelForm):
    class Meta:
        model = models.Add_Room
        fields = "__all__"

class Add_salary_form(forms.ModelForm):
    class Meta:
        model = models.Add_Salarys
        fields = "__all__"

