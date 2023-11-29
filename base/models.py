from django.db import models
from django.contrib.admin import ModelAdmin, register
from django.contrib.auth.models import User as AUser, BaseUserManager

# Create your models here.

class User(models.Model):
    user=models.ForeignKey(AUser, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    password=models.CharField(max_length=500,default="123")
    role=models.BooleanField()
    applicationstatus=models.IntegerField(default=0)
    otp=models. CharField(max_length=6,default="000000")
    def __str__(self):
        return self.name

class Applicant(models.Model):
    user=models.ForeignKey(AUser, on_delete=models.CASCADE,null=True)
    cgpa=models.FloatField(max_length=4,default=0.0)
    Roll=models.CharField(max_length=8)
    fathername=models.CharField( max_length=15)
    phone=models.CharField(max_length=12)
    altphone=models.CharField(max_length=12,default=0)
    cnic=models.CharField(max_length=15)
    email=models.EmailField(default="abc@gmail.com")
    city=models.CharField(max_length=11,default="None")
    address=models.CharField(max_length=15,default="None")
    postalcode=models.IntegerField(default=0000)
    profilephoto=models.ImageField(upload_to='profilephoto/',default="profilephoto/default.jpg")
    def __str__(self):
        return self.Roll

class DecisionMaker(models.Model):
    user=models.ForeignKey(AUser, on_delete=models.CASCADE,null=True)
    phone=models.CharField(max_length=11)
    cnic=models.CharField(max_length=14)
    def __str__(self):
        return self.cnic

class Application(models.Model):
    user=models.ForeignKey(AUser, on_delete=models.CASCADE,null=True)
    Roll=models.CharField(max_length=8,default="XXF-XXXX")
    SSC_Result=models.IntegerField(max_length=4)
    HSSC_Result=models.IntegerField(max_length=4)
    Father_NTN=models.CharField(max_length=25)
    electricityBill=models.IntegerField(default=0)
    gasBill=models.IntegerField(default=0)
    Income=models.IntegerField()
    Expenses=models.IntegerField()
    Property_Area=models.IntegerField()
    propertystatus=models.CharField(max_length=25)
    assets=models.IntegerField(default=0)
    siblings=models.IntegerField(default=0)
    siblingsEdufee=models.IntegerField(default=0)
    Description=models.CharField(max_length=500)
    ebilldoc=models.FileField(upload_to='ebilldoc/',default="ebilldoc/default.pdf")
    gbilldoc=models.FileField(upload_to='gbilldoc/',default="gbilldoc/default.pdf")
    transcript=models.FileField(upload_to='transcript',default="transcript/default.pdf")
    applicationstatus=models.IntegerField(default=0)
    aidamount = models.IntegerField(default=0)
    predicted_aid= models.IntegerField(default=0)
    def __str__(self):
        return self.Roll

class ReturnLoan(models.Model):
    user=models.ForeignKey(AUser, on_delete=models.CASCADE,null=True)
    transationmode=models.CharField(max_length=15)
    transactionid=models.CharField(max_length=15)
    transactiondate=models.DateField()
    transactionamount=models.IntegerField()
    transactionreceipt=models.FileField(upload_to='transactionreceipt',default="transactionreceipt/default.pdf")
    def __str__(self):
        return self.transactionid



class Support(models.Model):
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=20)
    description=models.CharField(max_length=500)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()


class FacultyVotes(models.Model):
    user = models.ForeignKey(AUser, on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=30)
    aidamount = models.CharField(max_length=30)
