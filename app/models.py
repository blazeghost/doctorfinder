from django.db import models
import datetime

# Create your models here.


class Master_Table(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    OTP = models.IntegerField()
    Role = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    is_created = models.DateTimeField(auto_now_add=True)


class Doctor(models.Model):
    m_id = models.ForeignKey(Master_Table, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.BigIntegerField(default="123")
    DOB = models.DateField(default="2020-12-01")
    Gender = models.CharField(max_length=50, default="SELECT")
    Address = models.CharField(max_length=100, default="Your Address")
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Intro = models.CharField(max_length=300, default="Your Intro")
    Experience = models.CharField(max_length=200)
    Education = models.CharField(max_length=200, default="Your Education")
    Designation = models.CharField(max_length=50)
    Specilazation = models.CharField(max_length=50)
    Working_hrs_start = models.TimeField(default=datetime.time(00, 00))
    Working_hrs_end = models.TimeField(default=datetime.time(00, 00))
    profile_pic = models.ImageField(
        upload_to="img/",  default='/img/default-user.jpg')
    ver_doc = models.FileField(
        upload_to="ver_doc/",  default='/ver_doc/default.pdf')


class Patient(models.Model):
    m_id = models.ForeignKey(Master_Table, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.BigIntegerField(default="123")
    DOB = models.DateField(default="2020-12-01")
    Gender = models.CharField(max_length=50, default="SELECT")
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    profile_pic = models.ImageField(
        upload_to="img/", default='/img/default-user.jpg')


class Hospital(models.Model):
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Hospitalname = models.CharField(max_length=50)
    foundingyear = models.IntegerField(default='2020')
    Contact = models.BigIntegerField(default="123")
    website = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Intro = models.CharField(max_length=200)
    hos_timing_from = models.TimeField(default=datetime.time(00, 00))
    hos_timing_to = models.TimeField(default=datetime.time(00, 00))
    logo = models.ImageField(
        upload_to="img/", default='/img/default-user.jpg')


class Appoinment(models.Model):
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Booking_date = models.DateField(default="2020-12-01")
    Booking_time = models.TimeField(default=datetime.time(00, 00))
    Visits = models.CharField(max_length=50)
    Message = models.CharField(max_length=100)
    Currentstatus = models.CharField(max_length=50, default="Pending")


class Case(models.Model):
    appoint_id = models.ForeignKey(Appoinment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    Currentstatus = models.CharField(max_length=50, default="Open")
    updated = models.DateTimeField(auto_now_add=True)
    Remarks = models.CharField(max_length=200)
    medical_history = models.CharField(max_length=200)
    allergic = models.CharField(max_length=200)
