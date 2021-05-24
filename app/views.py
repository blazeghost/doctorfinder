from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import *
from random import randint

# Create your views here.


def IndexPage(request):
    return render(request, "app/index.html")


# def RegisterPage(request):
#     return render(request, "app/register-user.html")


def RegisterPage(request):
    return render(request, "app/register-page.html")


def RegisterDoctorPage(request):
    return render(request, "app/register-doctor.html")


def RegisterPatientPage(request):
    return render(request, "app/register-user.html")


def RegisterDoctor(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['cpass']
    spec = request.POST['spec']
    city = request.POST['city']
    state = request.POST['state']
    role = "Doctor"

    testuser = Master_Table.objects.filter(Email=email)
    if testuser:
        message = "User is already exist"
        return render(request, "app/register-doctor.html", {'msg': message})
    else:
        if password == cpass:
            otp = randint(100000, 999999)
            masteruser = Master_Table.objects.create(
                Email=email, Password=password, OTP=otp, Role=role)
            newdoctor = Doctor.objects.create(
                m_id=masteruser, Firstname=fname, Lastname=lname, Specilazation=spec, City=city, State=state)

            message = "Doctor Successfully Registered"
            return render(request, "app/OTPverify.html", {'msg': message})
        else:
            message = "Password and Confirm Password doesnot match"
            return render(request, "app/register-doctor.html", {'msg': message})


def RegisterUser(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['cpass']

    role = "Patient"

    testuser = Master_Table.objects.filter(Email=email)
    if testuser:
        message = "User is already exist"
        return render(request, "app/register-user.html", {'msg': message})

    else:
        if password == cpass:
            otp = randint(100000, 999999)
            masteruser = Master_Table.objects.create(
                Email=email, Password=password, OTP=otp, Role=role)
            newpatient = Patient.objects.create(
                m_id=masteruser, Firstname=fname, Lastname=lname)

            message = "User Successfully Registered"
            return render(request, "app/OTPverify.html", {'msg': message})
        else:
            message = "Password and Confirm Password doesnot match"
            return render(request, "app/register-user.html", {'msg': message})


def OTPPage(request):
    return render(request, "app/OTPverify.html")


def OTPverify(request):

    email = request.POST['email']
    otp = int(request.POST['otpverify'])

    check = Master_Table.objects.get(Email=email)

    print("---------------===========>>>>", check.OTP)
    print("-------------===>>", otp)

    if check.OTP == otp:
        message = "OTP Verification Successfully"
        return render(request, 'app/login-2.html', {'msg': message})
    else:
        message = "Wrong OTP"
        return render(request, "app/OTPverify.html", {'msg': message})


def LoginPage(request):
    return render(request, "app/login-2.html")


def Login(request):
    if request.POST['role'] == "Doctor":
        email = request.POST['email']
        password = request.POST['password']

        testuser = Master_Table.objects.get(Email=email)

        if testuser:
            if testuser.Password == password and testuser.Role == "Doctor":
                doc = Doctor.objects.get(m_id=testuser)

                request.session['Role'] = testuser.Role
                request.session['id'] = testuser.id
                request.session['is_verified'] = testuser.is_verified
                request.session['Firstname'] = doc.Firstname
                request.session['Lastname'] = doc.Lastname
                request.session['Email'] = testuser.Email

                return render(request, "app/doctor/index.html")

            else:
                message = "User Password or Role Doesnot match"
                return render(request, "app/login-2.html", {'msg': message})

        else:
            message = "User not Found"
            return render(request, "app/login-2.html", {'msg': message})

    else:
        if request.POST['role'] == "Patient":
            email = request.POST['email']
            password = request.POST['password']

            testuser = Master_Table.objects.get(Email=email)

            if testuser:
                if testuser.Password == password and testuser.Role == "Patient":
                    user = Patient.objects.get(m_id=testuser)

                    request.session['Role'] = testuser.Role
                    request.session['id'] = testuser.id
                    request.session['Firstname'] = user.Firstname
                    request.session['Lastname'] = user.Lastname
                    request.session['Email'] = testuser.Email

                    return render(request, "app/index2.html")

                else:
                    message = "User Password or Role Doesnot match"
                    return render(request, "app/login-2.html", {'msg': message})

            else:
                message = "User not Found"
                return render(request, "app/login-2.html", {'msg': message})


def AdminLogin(request):
    return render(request, "app/admin/login.html")


def AdminLoginCheck(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":
        request.session['username'] = username
        request.session['password'] = password
        return render(request, "app/admin/index.html")
    else:
        message = "Username or Password doesnot match"
        return render(request, "app/admin/login.html", {'msg': message})


def PatientLogout(request):

    del request.session['Role']
    del request.session['id']
    del request.session['Firstname']
    del request.session['Email']

    return render(request, "app/index.html")


def DoctorLogout(request):

    del request.session['Role']
    del request.session['id']
    del request.session['Firstname']
    del request.session['Email']
    del request.session['is_verified']

    return render(request, "app/index.html")


def AdminLogout(request):

    del request.session['username']
    del request.session['password']

    return render(request, "app/index.html")


def ProfilePage(request, pk):
    udata = Master_Table.objects.get(id=pk)
    if udata.Role == "Doctor":
        doc = Doctor.objects.get(m_id=udata)
        request.session['Email'] = udata.Email
        return render(request, "app/doctor/doctor-profile.html", {'key1': doc})
    else:
        if udata.Role == "Patient":
            user = Patient.objects.get(m_id=udata)
            request.session['Email'] = udata.Email
            return render(request, "app/user-profile.html", {'key1': user})


def UpdateProfile(request, pk):
    udata = Master_Table.objects.get(id=pk)

    if udata.Role == "Doctor":
        doc = Doctor.objects.get(m_id=udata)
        doc.Firstname = request.POST['fname']
        doc.Lastname = request.POST['lname']
        doc.City = request.POST['city']
        doc.State = request.POST['state']
        doc.Contact = request.POST['contact']
        # print("------------------------------->>>>>", doc.Contact)
        doc.DOB = request.POST['dob']
        doc.profile_pic = request.FILES['pro-pic']
        doc.Gender = request.POST['gender']
        doc.Intro = request.POST['intro']
        doc.Experience = request.POST['exp']
        doc.Education = request.POST['edu']
        doc.Designation = request.POST['designation']
        doc.Specilazation = request.POST['spec']
        doc.Working_hrs_start = request.POST['work-hrs-start']
        doc.Working_hrs_end = request.POST['work-hrs-end']
        doc.ver_doc = request.FILES['verdoc']

        doc.save()
        url = f"/profilepage/{pk}"
        return redirect(url)
    else:
        if udata.Role == "Patient":
            user = Patient.objects.get(m_id=udata)
            user.Firstname = request.POST['fname']
            user.Lastname = request.POST['lname']
            user.City = request.POST['city']
            user.State = request.POST['state']
            user.Contact = request.POST['contact']
            user.DOB = request.POST['dob']
            user.profile_pic = request.FILES['pro-pic']
            user.Gender = request.POST['gender']
            user.save()
            url = f"/profilepage/{pk}"
            return redirect(url)

            # return HttpResponseRedirect(reverse('url'))
            # return render(request, "app/user-profile.html")


def AddHospitalPage(request, pk):
    mdata = Master_Table.objects.get(id=pk)
    doc_id = Doctor.objects.get(m_id=mdata)
    test = Hospital.objects.filter(doc_id=doc_id)
    # print("===-===-=-==-===>>>>>>>>>>>>>", test)
    if test:

        if mdata.Role == "Doctor":

            hosp = Hospital.objects.get(doc_id=doc_id)
            return render(request, "app/doctor/add-hospital.html", {'key1': hosp})
    else:

        return render(request, "app/doctor/add-hospital.html")


def AddHospitalData(request, pk):
    mdata = Master_Table.objects.get(id=pk)
    doc_id = Doctor.objects.get(m_id=mdata)
    test = Hospital.objects.filter(doc_id=doc_id)
    if test:

        if mdata.Role == "Doctor":
            hosp = Hospital.objects.get(doc_id=doc_id)
            hosp.Hospitalname = request.POST['hospitalname']
            hosp.foundingyear = request.POST['foundingyear']
            hosp.Contact = request.POST['contact']
            hosp.website = request.POST['website']
            hosp.City = request.POST['city']
            hosp.State = request.POST['state']
            hosp.Intro = request.POST['intro']
            hosp.hos_timing_from = request.POST['hos_timing_from']
            hosp.hos_timing_to = request.POST['hos_timing_to']
            hosp.logo = request.FILES['logo']

            hosp.save()
            message = "Hospital Successfully Added"
            url = f"/addhospitalpage/{pk}"
            return redirect(url)
    else:
        # print("--------------------> Fail")
        if mdata.Role == "Doctor":
            hospitalname = request.POST['hospitalname']
            foundingyear = request.POST['foundingyear']
            contact = request.POST['contact']
            website = request.POST['website']
            city = request.POST['city']
            state = request.POST['state']
            intro = request.POST['intro']
            hos_timing_from = request.POST['hos_timing_from']
            hos_timing_to = request.POST['hos_timing_to']
            logo = request.FILES['logo']

            newhosps = Hospital.objects.create(doc_id=doc_id,
                                               Hospitalname=hospitalname, foundingyear=foundingyear, Contact=contact, website=website,
                                               City=city, State=state, Intro=intro,
                                               hos_timing_from=hos_timing_from, hos_timing_to=hos_timing_to, logo=logo)

            message = "Hospital Successfully Added"
            url = f"/addhospitalpage/{pk}"
            return redirect(url)


def DoctorListPage(request):
    doc = Doctor.objects.all()

    return render(request, "app/doctor-list.html", {"key1": doc})


def DetailListPage(request, pk):
    doc = Doctor.objects.get(id=pk)
    return render(request, "app/detail-page.html", {"key1": doc})


def PatientAppoinment(request, pk):
    mdata = Master_Table.objects.get(id=pk)
    # doc = Doctor.objects.get(m_id=mdata)
    pat = Patient.objects.get(m_id=mdata)

    doc_id = request.POST["doctorid"]

    doc = Doctor.objects.get(id=doc_id)

    b_date = request.POST["booking_date"]
    b_time = request.POST["booking_time"]
    b_visit = request.POST["booking_visit"]
    b_message = request.POST["booking_message"]

    newappoint = Appoinment.objects.create(
        patient_id=pat, doc_id=doc, Booking_date=b_date, Booking_time=b_time, Visits=b_visit, Message=b_message)

    # url = f"/detaillistpage/{pk}"
    # return redirect(url)
    return render(request, "app/confirm.html")


def DocBookingCheck(request):
    # mdata = Master_Table.objects.get(id=pk)
    # doc = Doctor.objects.get(m_id=mdata)

    appoint = Appoinment.objects.all()

    return render(request, "app/doctor/bookings.html", {'key1': appoint})


def DocBookingApprove(request, pk):
    appoint = Appoinment.objects.get(id=pk)
    appoint.Currentstatus = "Approved"
    appoint.save()

    url = f"/docbookingcheck/"
    return redirect(url)
    # return render(request, "app/doctor/bookings.html")


def DocBookingCancel(request, pk):
    appoint = Appoinment.objects.get(id=pk)
    appoint.Currentstatus = "Cancel"
    appoint.save()

    url = f"/docbookingcheck/"
    return redirect(url)
    # return render(request, "app/doctor/bookings.html")


def ConfirmPage(request):
    return render(request, "app/confirm.html")


def Error404(request):
    return render(request, "app/404.html")


def AboutUs(request):
    return render(request, "app/about.html")


def ContactUs(request):
    return render(request, "app/contacts.html")


def FAQ(request):
    return render(request, "app/faq1.html")


def FAQPage(request):
    return render(request, "app/faq2.html")


def DocIndex(request):
    return render(request, "app/doctor/index.html")


def Admin_Doc_List(request):

    doc_data = Doctor.objects.all()

    return render(request, "app/admin/doc-list.html", {'key_doc': doc_data})


def Doc_CheckPage(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    doc_data = Doctor.objects.get(m_id=m_data)
    return render(request, "app/admin/doc-check.html", {'key_doc': doc_data})


def Doc_Check(request, pk):
    m_data = Master_Table.objects.get(id=pk)

    m_data.is_verified = request.POST['is_verified']
    m_data.is_active = request.POST['is_active']

    m_data.save()

    url = f"/doc-checkpage/{pk}"
    return redirect(url)


def DocDelete(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    m_data.delete()
    return HttpResponseRedirect(reverse('admin-doc-list'))


def LoginIndex(request):
    return render(request, "app/index2.html")


def Doc_PatientProfile(request, pk):
    patient = Patient.objects.get(id=pk)
    return render(request, "app/doctor/patient-profile.html", {'key1': patient})


def DocBase(request):
    appoint = Appoinment.objects.all()

    return render(request, 'app/doctor/base1.html')


def myappointlist(request):
    myappoint = Appoinment.objects.all()

    return render(request, 'app/my-appointment.html', {'key1': myappoint})


def blog(request):
    return render(request, 'app/blog-1.html')


def Doc_Case(request):
    case = Case.objects.all()

    return render(request, 'app/doctor/case.html', {'key1': case})


def New_Case(request):

    app_id = request.POST['app_id']

    appoint = Appoinment.objects.get(id=app_id)

    testcase = Case.objects.filter(appoint_id=appoint)

    if testcase:
        message = "Case already exists"

        return render(request, 'app/doctor/messages.html', {'msgcase': message})
    else:
        newcase = Case.objects.create(appoint_id=appoint)

        # url = f"/docbookingcheck/"
        # return redirect(url)
        message = "Case Successfully Created"
        return render(request, 'app/doctor/messages.html', {'msgcase': message})


def Doc_CaseDetails(request, pk):

    case = Case.objects.get(id=pk)

    return render(request, 'app/doctor/case-details.html', {'key1': case})


def Doc_CaseClose(request, pk):
    case = Case.objects.get(id=pk)
    case.Currentstatus = "Closed"
    case.save()

    url = f"/doc-case/"
    return redirect(url)


def Doc_UpdateCase(request, pk):
    case = Case.objects.get(id=pk)
    case.medical_history = request.POST['medical_history']
    case.allergic = request.POST['allergic']
    case.Remarks = request.POST['remarks']
    case.save()

    url = f"/doc-casedetails/{pk}"
    return redirect(url)


def CaseList(request):
    case = Case.objects.all()
    return render(request, 'app/my-case.html', {'key1': case})


def CaseDetails(request, pk):
    case = Case.objects.get(appoint_id=pk)
    return render(request, 'app/my-casedetails.html', {'key1': case})


def UpdateCase(request, pk):
    case = Case.objects.get(id=pk)
    case.medical_history = request.POST['medical_history']
    case.allergic = request.POST['allergic']
    x = case.appoint_id.id
    print(x)
    case.save()

    url = f"/casedetails/{case.appoint_id.id}"

    return redirect(url)


# def Homesearch(request):

#     search_term = ''

#     if 'search' in request.GET:

#         search_term = request.GET['search']
#         print("------------........>>>", search_term)
#     search_value = request.POST['search']

#     doc = Doctor.objects.all().filter(Firstname=search_value)

#     return render(request, 'app/search-result.html')
