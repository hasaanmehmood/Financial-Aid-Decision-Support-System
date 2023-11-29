from django.shortcuts import render
from base.models import Note
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from base.models import Applicant
from base.models import Application,FacultyVotes
from base.models import User
from base.models import Support
from base.models import ReturnLoan as RLoan
from base.models import DecisionMaker
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#from base.models import User as AUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage,get_connection
from django.contrib.auth.models import User as AUser
from django.conf import settings
import random,string
import threading
from django.contrib import messages
from backend.settings import EMAIL_HOST_USER
import numpy as np
import json
import os
from collections import Counter
import pandas as pd

from django.core.files.storage import default_storage

# Create your views here.
def Landing(request):
    #mydata = User.objects.filter(name='hasaan', password='1234').values()
    #print(mydata)
    #obj=Note.objects.all()
    #print(obj)
    #print(obj[0].user)
    return render(request, 'landing.html')

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')



@login_required
def LogoutPage(request):
    logout(request)
    return render (request,'landing.html')

@login_required
def ApplyAid(request):
    n=request.user
    user1=AUser.objects.get(username=n)
    if(Application.objects.filter(user=user1).exists()):
        messages.error(request,'You have already applied for aid, Check your Status')
        return redirect('userdash')
    if request.method=='POST':
        username=request.user

        email=request.POST.get("email")
        role=0
        roll=request.POST.get("roll")
        father=request.POST.get("fname")
        phone=request.POST.get("phone")
        alt=request.POST.get("phone2")
        cnic=request.POST.get("cnic")
        cgpa=request.POST.get("cgpa")
        address=request.POST.get("address")
        city=request.POST.get("city")
        postal=request.POST.get("post-code")
        ssc=request.POST.get("ssc")
        hssc=request.POST.get("hssc")
        fntn=request.POST.get("ntn")
        income=request.POST.get("income")
        expense=request.POST.get("expense")
        bill=request.POST.get("bill")
        gbill=request.POST.get("gbill")
        status=request.POST.get("prop-type0")
        print(status)
        parea=request.POST.get("area")
        asset=request.POST.get("assets")
        siblingfee=request.POST.get("siblingfee")
        photo=request.POST.get("pic")

        if 'pic' in request.FILES:
            file = request.FILES['pic']
            file_name = file.name
            default_storage.save(file_name,file)
        
        dbill=request.POST.get("bill")    
        if 'bill' in request.FILES:
            file = request.FILES['bill']
            file_name1 = file.name
            default_storage.save(file_name,file)

        dgbill=request.POST.get("dgbill")
        if 'dgbill' in request.FILES:
            file = request.FILES['dgbill']
            file_name2 = file.name
            default_storage.save(file_name,file)

        transcrpt=request.POST.get("transcript")
        if 'transcript' in request.FILES:
            file = request.FILES['transcript']
            file_name3 = file.name
            default_storage.save(file_name,file)
        
        sibling=request.POST.get("siblings")
        comment=request.POST.get("comments")
        #user1=User(name=username,email=email,role=role)
        user_instances = AUser.objects.all()
        i=AUser.objects.get(username=username)
        
        u = get_user_model()
        n=request.user
        user1=AUser.objects.get(username=n)
        if(Application.objects.filter(user=user1).exists()):
            messages.error(request,'You have already applied for aid')
            return redirect('userdash')
        else:
            admin_obj=User.objects.filter(user=i).first()
            admin_obj.applicationstatus=1
            admin_obj.save()
            from tensorflow.keras.models import load_model
            import tensorflow as tf
            
            
            print(dbill)
            df = pd.DataFrame({
            'electricity_bills': int(dbill),
            'land_ownership': np.random.choice([0, 1], size=1),
            'family_income': income,
            'family_assets': asset,
            'expenditures': expense,
            'siblings_education_status': np.random.choice([0, 1, 2], size=1),
            'gas_bills': gbill,
            'high_school_marks': hssc,
            'current_cgpa': cgpa,
            'previous_aid_amount': np.random.randint(0, 1000, size=1),
            'property_status': np.random.choice([0, 1], size=1),
            'property_status_0': np.random.choice([0, 1], size=1),
            'parent_guardian_deceased': np.random.choice([0, 1], size=1),
            'parent_guardian_deceased_0': np.random.choice([0, 1], size=1),
            'siblings_education_fee': siblingfee,
            'owned_land_valuation': parea,
        })

            from sklearn.preprocessing import StandardScaler

            X_encoded = pd.get_dummies(df, columns=['property_status', 'parent_guardian_deceased'])
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X_encoded)
            

            data = np.array([
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1, 2], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.randint(0, 1000, size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
                np.random.choice([0, 1], size=1),
            ])

            data  = np.expand_dims(data,axis=1)

            # numpy_array = data.astype('float32').to_numpy()  # Convert DataFrame to NumPy array
            # tensor = tf.convert_to_tensor(numpy_array)
            # print(df)

            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, 'model.h5')
            model = load_model(file_path)
            predicted = model.predict(X_scaled)[0]








            #usero=User.objects.create(username=user1.username,email=user1.email,role=0,password=user1.password)
            applicant = Applicant.objects.create(user=i, altphone=alt, Roll=roll,address=address,cgpa=cgpa, fathername=father,profilephoto=file_name, phone=phone, cnic=cnic, email=email, city=city, postalcode=int('0' + postal))
            #applciant=Applicant(user=usero,altphone=alt,Roll=roll,fathername=father,phone=phone,cnic=cnic,email=email,city=city,postalcode=postal)
            #applicant.save()
            #application=Application(user=usero,Roll=roll,SSC_Result=ssc,HSSC_Result=hssc,Father_NTN=fntn,electricityBill=bill,gasBill=gbill,propertystatus=status,assets=asset,siblingsEdufee=siblingfee,ebilldoc=egbill,gbilldoc=dgbill,Income=income,Expenses=expense,Property_Area=parea,siblings=sibling,Description=comment,transcript=transcrpt)
            application = Application.objects.create(user=i, Roll=roll, SSC_Result=int('0' + ssc), HSSC_Result=int('0' + hssc), Father_NTN=fntn, electricityBill=int('0' + bill), gasBill=int('0' + gbill), propertystatus=status, assets=int('0' + asset), siblingsEdufee=int('0' + siblingfee), ebilldoc=dbill, gbilldoc=dgbill, Income=int('0' + income), Expenses=int('0' + expense), Property_Area=int('0' + parea), siblings=int('0' + sibling), Description=comment, transcript=transcrpt,applicationstatus=1,aidamount=0,predicted_aid=predicted)
            application.save()
            return render(request, 'userdash.html',{'username':n})
   
    return render (request,'applyaid.html')

def Help(request):
    if request.method=='POST':
        username=request.POST.get("name")
        email1=request.POST.get("email")
        desc=request.POST.get("description")
        query=Support(name=username,email=email1,description=desc)
        query.save()

        query_email=request.POST['email']
        #admin_obj=AUser.objects.filter(email=query_email,is_staff=0).first()
        #ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6)) # generate random string
        #ran_encrypted=make_password(ran)
        #admin_obj.password=ran_encrypted
        #admin_obj.save()
        adminmail='f190249@nu.edu.pk'
        email = EmailMessage(
                'Query '+username+' '+email1, 
                desc+'\n\n\n'+'username: '+username+'\n'+'email: '+email1+'\n', 
                EMAIL_HOST_USER, 
                [adminmail],
            ) 
        send_email = threading.Thread(target=email.send())
        send_email.start()
        messages.error(request, 'Please Check Your Given Email ')
        return render(request, 'landing.html')

    return render(request, 'help.html')
@login_required
def FacultyDash(request):
    user = request.session.get('username')
    context = {'username': user}
    return render(request, 'facultydash.html', context)

def FacultyLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        user=username.upper()
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1,role=1)
        #user=authenticate(request,username=username,password=pass1)
       
        if user is not None:
            login(request,user)
            return render(request, 'facultydash.html',{'username':user})
        else:
            #return alert("Username/Password is incorrect")
            messages.error(request,'username or password not correct')
            return redirect('flogin')
            #return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'flogin.html')

@login_required
def ViewProfile(request):
    u= request.user
    user1 = AUser.objects.get(username=u)
    application= Application.objects.filter(user = AUser.objects.filter(username=user1)[0]).first()
    applicant = Applicant.objects.filter(user = AUser.objects.filter(username=user1)[0]).first()
    context = {'username': u ,'applicant': applicant, 'application': application}
    return render(request, 'ViewProfile.html', context) 

def Landing(request):
    return render(request, 'landing.html')

def signup_login_view(request):

    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            encryptedpassword=make_password(password)
            MyUser = get_user_model()
            if username and MyUser.objects.filter(username__iexact=username).exists():
                messages.error(request, f"User {username} already exist!")
                print("Username already exists")
                #raise forms.ValidationError(error_messages["unique"], code="unique")
                return render(request,'signup_login.html')
            elif username == '':
                return render(request,'signup_login.html')
            else:
                user = AUser.objects.create(username=username, email=email, password=encryptedpassword)
                user.save()
                U=User.objects.create(user=user,name=username, email=email, password=password,role=0,applicationstatus=0)
                #user = User.objects.create_user(username=username, email=email, password=password)
                U.save()
                request.session['username'] = username
                login(request,user)
                return render(request, 'userdash.html',{'username':user})
        
        elif 'login' in request.POST:
            print(request.POST.get('username'))
            print(request.POST.get('password'))
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                request.session['username'] = username
                login(request,user)
                return render(request, 'userdash.html',{'username':user})
            else:
                messages.error(request, f"User {username} does not exist!")
                return render(request,'signup_login.html')

    return render(request, 'signup_login.html')
@login_required
def user_dashboard(request):  
    user = request.session.get('username')
    context = {'username': user}
    return render(request, 'userdash.html',context)  # pass the username to the template


def ForgetPass(request):
    username = request.session.get('username')
    if request.POST:
        forget_email = request.POST.get('email1')
        admin_obj=AUser.objects.filter(email=forget_email,is_staff=0).first()
        if admin_obj:
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6)) # generate random string
            ran_encrypted=make_password(ran)
            admin_obj.password=ran_encrypted
            admin_obj.save()
            email = EmailMessage(
                'Password reset', 
                'You are receiving this Email because you requested a password reset for your user account at FADSS..\n'+admin_obj.username +' your New Password is :' + ran, 
                EMAIL_HOST_USER, 
                [forget_email],
                ) 
            send_email = threading.Thread(target=email.send())
            send_email.start()
            #digits = [i for i in range(0, 10)]
            ## initializing a string
            #random_str = ""
            ## we can generate any lenght of string we want
            #for i in range(6):
                #index=math.floor(random.random() * 10)
                #random_str += str(digits[index])
            ## generating a random index
            ## if we multiply with 10 it will generate a number between 0 and 10 not including 10
            ## multiply the random.random() with length of your base list or str
            #gotp=random_str
            #obj=User.objects.filter(email=forget_email).update(otp=gotp)
            #obj.save()
            #email = EmailMessage(
                #'Password reset', 
                #'You are receiving this Email because you requested a password reset for your user account at FADSS..\n'+gotp +' is your OTP for password reset', 
                #EMAIL_HOST_USER, 
                #[forget_email],
            #) 
            #send_email = threading.Thread(target=email.send())
            #context={'username':username,'email':forget_email,'otp':gotp}
            #print('otp is '+gotp)
            #print('email is '+forget_email)
            return render(request, 'signup_login.html')
        else:
            messages.error(request, f"No user found with email address {forget_email}. Please check your email and try again.")
            return render(request,'change_password.html',{'username': username})
    return render(request,'change_password.html',{'username': username})
                                          




def SendOtp(request):
    e=request.get('email')
    digits = [i for i in range(0, 10)]
    ## initializing a string
    random_str = ""
    ## we can generate any lenght of string we want
    for i in range(6):
        index=math.floor(random.random() * 10)
        random_str += str(digits[index])
            ## generating a random index
            ## if we multiply with 10 it will generate a number between 0 and 10 not including 10
            ## multiply the random.random() with length of your base list or str
    gotp=random_str
    User.objects.filter(email=e).update(otp=gotp)
    forget_email=email
    email = EmailMessage(
                'Password reset', 
                'You are receiving this Email because you requested a password reset for your user account at FADSS..\n'+otp +' is your OTP for password reset', 
                EMAIL_HOST_USER, 
                [forget_email],
            ) 
    send_email = threading.Thread(target=email.send())
    send_email.start()
    return
@login_required
def ViewStatus(request):
    username = request.user
    obj = User.objects.get(name=username)
    #obj = User.objects.filter(user = AUser.objects.filter(username=username)[0]).first()
    applicationstatus = obj.applicationstatus
    status=''
    if applicationstatus == 3:
            status = Application.objects.filter(user_id=username.id).last().applicationstatus

    if status == '1':
            status = 'Approved'
    if status =='2':
            status="Rejected"
    context = {'username': username, 'applicationstatus':applicationstatus,'status':status }
    return render(request, 'ViewStatus.html', context)

@login_required
def ViewReport(request):  
    user = request.session.get('username')
    context = {'username': user}
    return render(request, 'viewReport.html',context)
@login_required
def ViewReport(request,id,):
    if request.method =='POST':
        status = request.POST.get('fstatus')
        amount = request.POST.get('aid_amount')
        aid_id = request.POST.get('aid_id')
        user = request.user
        user = AUser.objects.get(username=user)
        appli = Application.objects.get(pk=aid_id)
        applicant = Applicant.objects.get(pk=aid_id)
        new_vaote =FacultyVotes(status=status,aidamount=amount,user=user,application=appli)
        new_vaote.save()
        vote_list =FacultyVotes.objects.filter(application_id=aid_id).all().values_list('status', flat=True)
        print(vote_list)
        if(len(vote_list)>=3):
            counter = Counter(vote_list)
            most_common_value = counter.most_common(1)[0][0]
            print(most_common_value)
            fsum = FacultyVotes.objects.filter(application_id=aid_id).all().values_list('aidamount', flat=True)
            total=0
            for i in fsum:
                total = total +int(i)
            amount = total/3
            apli = Application.objects.get(pk=aid_id)
            if most_common_value =='approved':
                apli.applicationstatus = 1
            else:
                apli.applicationstatus = 2
            apli.aidamount = amount
            apli.save()
            uu = User.objects.get(user_id=appli.user_id)
            uu.applicationstatus = 3
            uu.save()

        else:
            uu = User.objects.get(user_id=appli.user_id)
            uu.applicationstatus = 2
            uu.save()
        
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        user = request.user
        user = AUser.objects.get(username=user)
        print(user.id)
        application = Application.objects.get(pk=id)
        applicant = Applicant.objects.get(pk=id)
        print(application.id)
        voted = not FacultyVotes.objects.filter(application_id=id).filter(user_id=user.id).exists()
        print(voted)
        context = {'application': application,'applicant': applicant, 'voted':voted}
    return render(request, 'viewReport.html',context)
@login_required
def ViewCandidates(request):
    if request.method == 'POST':
        
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        applications = Application.objects.all()
        applicant = Applicant.objects.all()
        field_names = [field.name for field in Application._meta.get_fields()]
        field_names1 = [field.name for field in Applicant._meta.get_fields()]
        print(applications)
        return render(request, 'CandidateList.html',context={'applications':applications,'field_names':field_names})
@login_required

def ReturnLoan(request):
    u= request.session.get('username')
    if(request.method=='POST'):
        pmode=request.POST.get("mode")
        pamount=request.POST.get("amount")
        psource=request.POST.get("source")
        pdate=request.POST.get("date")
        pslip=request.POST.get("slip")
        if 'slip' in request.FILES:
            file = request.FILES['slip']
            file_name = file.name
            default_storage.save(file_name,file)
        print(pmode)
        print(pamount)
        print(psource)
        print(pdate)
        print(pslip)
        i=AUser.objects.get(username=u)
        rl = RLoan.objects.create(user=i, transationmode=pmode, transactionid=psource, transactiondate=pdate, transactionamount=pamount, transactionreceipt=pslip)
        rl.save()
    #user = request.session.get('username')
    #context = {'username': username}
        return render(request, 'userdash.html',{'username':u})
    return render(request, 'returnLoan.html')