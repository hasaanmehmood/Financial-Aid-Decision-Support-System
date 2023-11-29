from django.contrib import admin
from .models import User
from .models import Applicant
from .models import DecisionMaker
from .models import Application

from .models import ReturnLoan

# Register your models here.
class user_admin(admin.ModelAdmin):
    search_fields=('name',) 

class applicant_admin(admin.ModelAdmin):
    search_fields=('Roll',) 

class application_admin(admin.ModelAdmin):
    search_fields=('Roll',) 

class decision_admin(admin.ModelAdmin):
    search_fields=('cnic',) 

class returnLoan_admin(admin.ModelAdmin):
    search_fields=('transactionid',) 


admin.site.register(ReturnLoan,returnLoan_admin)
admin.site.register(User,user_admin)
admin.site.register(Applicant,applicant_admin)
admin.site.register(Application,application_admin)
admin.site.register(DecisionMaker,decision_admin)