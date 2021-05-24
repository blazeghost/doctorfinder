from django.urls import path, include
from . import views

urlpatterns = [

    # Page URLS
    path("", views.IndexPage, name="index"),
    path("registerpage/", views.RegisterPage, name="registerpage"),
    path("registerdoctorpage/", views.RegisterDoctorPage,
         name="registerdoctorpage"),
    path("registerpatientpage/", views.RegisterPatientPage,
         name="registerpatientpage"),
    path("loginpage/", views.LoginPage, name="loginpage"),
    path("adminloginpage/", views.AdminLogin, name="adminloginpage"),
    path("profilepage/<int:pk>", views.ProfilePage, name="profilepage"),
    path("addhospitalpage/<int:pk>", views.AddHospitalPage, name='addhospitalpage'),
    path("doctorlist/", views.DoctorListPage, name="doctorlist"),
    path("detaillistpage/<int:pk>", views.DetailListPage, name="detaillistpage"),
    path("docbookingcheck/", views.DocBookingCheck, name="docbookingcheck"),
    path("confirmpage/", views.ConfirmPage, name="confirmpage"),
    path("error404/", views.Error404, name="error404"),
    path("aboutus/", views.AboutUs, name="aboutus"),
    path("contacts/", views.ContactUs, name="contacts"),
    path("faq/", views.FAQ, name="faq"),
    path("faqpage/", views.FAQPage, name="faqpage"),
    path("docindex/", views.DocIndex, name="docindex"),
    path("loginindex/", views.LoginIndex, name="loginindex"),
    path("doc-patientprofile/<int:pk>", views.Doc_PatientProfile,
         name="doc-patientprofile"),
    path("docbase/", views.DocBase, name="docbase"),
    path("otppage/", views.OTPPage, name="otppage"),
    path('myappoint/', views.myappointlist, name='myappoint'),
    path('blog/', views.blog, name='blog'),
    path('doc-case/', views.Doc_Case, name='doc-case'),
    path('doc-casedetails/<int:pk>', views.Doc_CaseDetails, name='doc-casedetails'),
    path('caselist/', views.CaseList, name="caselist"),
    path('casedetails/<int:pk>', views.CaseDetails, name='casedetails'),




    # Functionality URLS
    path("registerdoctor/", views.RegisterDoctor, name="registerdoctor"),
    path("registeruser/", views.RegisterUser, name="registeruser"),
    path("login/", views.Login, name="login"),
    path("adminlogin/", views.AdminLoginCheck, name="adminlogin"),
    path("patientlogout/", views.PatientLogout, name="patientlogout"),
    path("doctorlogout/", views.DoctorLogout, name="doctorlogout"),
    path("adminlogout/", views.AdminLogout, name="adminlogout"),
    path('updateprofile/<int:pk>', views.UpdateProfile, name="updateprofile"),
    path("addhospitaldata/<int:pk>", views.AddHospitalData, name='addhospitaldata'),
    path("patientappoint/<int:pk>", views.PatientAppoinment, name="patientappoint"),
    path("docbookingapprove/<int:pk>",
         views.DocBookingApprove, name="docbookingapprove"),
    path("docbookingcancel/<int:pk>",
         views.DocBookingCancel, name="docbookingcancel"),
    path("admin-doc-list/", views.Admin_Doc_List, name="admin-doc-list"),
    path('doc-checkpage/<int:pk>', views.Doc_CheckPage, name="doc-checkpage"),
    path("doc-check/<int:pk>", views.Doc_Check, name="doc-check"),
    path("doc-delete/<int:pk>", views.DocDelete, name="doc-delete"),
    path('otpverify/', views.OTPverify, name='otpverify'),
    path('newcase/', views.New_Case, name='newcase'),
    path('doc-caseclosed/<int:pk>', views.Doc_CaseClose, name='doc-caseclosed'),
    path('doc-updatecase/<int:pk>', views.Doc_UpdateCase, name='doc-updatecase'),
    path('updatecase/<int:pk>', views.UpdateCase, name='updatecase'),
    #     path('searchresult/', views.Homesearch, 'searchresult'),



]
