from django.contrib import admin
from .models import Form


# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display=('name','age','dob','fathername','mobile','email','password','city','address')
admin.site.register(Form,FormAdmin)