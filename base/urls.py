from django.urls import path
from .views import Landing
from . import views
from django.contrib.auth import views as auth_view
from base import views
urlpatterns = [
    path('',Landing,name="Landing"),
    path('landing/',views.Landing,name='landing'),
    #path('signup/',views.SignupPage,name='signup'),
    #path('login/',views.user_dashboard,name='login'), 
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('applyaid/',views.ApplyAid,name='applyaid'),
    path('help/',views.Help,name='help'),
    path('flogin/',views.FacultyLogin,name='flogin'),
    path('forget/',views.ForgetPass,name='forgetpass'),
    path('viewprofile/',views.ViewProfile,name='viewprofile'),
    path('viewstatus/',views.ViewStatus,name='viewstatus'),
    path('viewreport/',views.ViewReport,name='viewreport'),
    path('returnloan/',views.ReturnLoan,name='returnloan'),
    path('viewreports/<int:id>/',views.ViewReport,name='viewreports'),
    path('viewcandidates/',views.ViewCandidates,name='viewcandidates'),
    path('facultydash/',views.FacultyDash,name='facultydash'),
    #path('signup_login/', views.signup_login_view, name='signup_login')
    path('signup_login/', views.signup_login_view, name='signup_login'),
    path('userdash/', views.user_dashboard, name='userdash')]