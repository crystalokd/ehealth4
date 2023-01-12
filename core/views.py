from django.shortcuts import render, redirect
from .models import User, Profile, Appointment
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.


def appointment_approval(request):
	# Get Counts
	total_count = Appointment.objects.all().count()
	approved_count = Appointment.objects.filter(approved=True).count()

	me = request.user.email
	# appointments = Appointment.objects.filter(doc_email=me)
	appointments = Appointment.objects.all()
	if request.user.is_physician:
		if request.method == "POST":

			# Get list of checked box id's
			id_list = request.POST.getlist('boxes')

			# Uncheck all events
			appointments.update(approved=False)


			# Update the database
			for x in id_list:
				Appointment.objects.filter(pk=int(x)).update(approved=True)

			# Show Success Message and Redirect
			messages.success(request, ("Event List Approval Has Been Updated!"))
			return redirect('appointment-approval')
		else:
			return render(request, 'core/appointment_approval.html', {'appointments':appointments, 'total_count':total_count, 'approved_count':approved_count})
	else:
		messages.success(request, ("You aren't authorized to view this page!"))
		return redirect('home-page')
	return render(request, 'core/appointment_approval.html')






def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_schedule = request.POST['your-schedule']
		your_message = request.POST['your-message']
		doc_email = request.POST['doc-email']

		# send an email
		appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Schedule: " + your_schedule + " Message: " + your_message


		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			[doc_email], # To Email
			)

		return render(request, 'core/appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_schedule': your_schedule,
			'your_message': your_message
			})
	else:
		return render(request, 'core/home.html', {})







def show_doc(request, doc_id):
	doctor = User.objects.get(pk=doc_id)
	return render(request, 'core/show_doc.html', {'doctor':doctor})

def search_doc(request):
	if request.method == "POST":
		searched = request.POST['searched']
		doctors = User.objects.filter( is_physician=True)
		return render(request, 'core/search_doc.html', {'searched':searched,
			'doctors':doctors})
	else:
		return render(request, 'core/search_doc.html', {})
	 




@login_required
def HomePage(request):
	profile = request.user.first_name
	if request.user.is_physician==False:
		tmp = 'core/base.html'
	else:
		tmp = 'core/base2.html'
	context = {
	    'profile': profile,
	    'tmp': tmp,
	}
	return render (request, 'core/index.html', context)

def FirstPage(request):
	return render (request, 'core/home.html', {})


def Register(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		password = request.POST.get('password')
		mobile = request.POST.get('phone')


		new_user = User.objects.create_user(first_name=fname,last_name = lname, email=email, mobile=mobile, password=password)

		new_user.save()
		return redirect('login-page')
	return render (request, 'core/register.html', {})

def RegisterDoc(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		password = request.POST.get('password')
		mobile = request.POST.get('phone')

		new_user = User.objects.create_user(first_name=fname,last_name = lname, email=email, mobile=mobile, password=password, is_physician=True)

		new_user.save()
		return redirect('login-page')
	return render (request, 'core/registerMed.html', {})









def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'core/login.html', {})



def add_profile(request):
	submitted = False
	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.owner = request.user.id
			profile.save()
			submitted = True

			render(request, 'core/profile.html', {'form': form, 'submitted':submitted})
	else:
		form = ProfileForm
		

	return render(request, 'core/profile.html', {'form': form, 'submitted':submitted})







def chart(request):
	users= Profile.objects.all()
	Stomach_ach_number, Diarrheal_number, Injuries_number, Head_ache_number, Cough_number = 0,0,0,0,0
	for i in users:
	    if i.Stomach_ach=='Yes':
	        Stomach_ach_number += 1
	    if i.Diarrheal=='Yes':
	        Diarrheal_number += 1
	    if i.Injuries=='Yes':
	        Injuries_number += 1
	    if i.Head_ache=='Yes':
	        Head_ache_number += 1
	    if i.Cough=='Yes':
	        Cough_number += 1
	data = [Stomach_ach_number, Diarrheal_number, Injuries_number, Head_ache_number, Cough_number]

	return render(request, 'core/chart.html', {'data':data})


def table(request):
	user_list = Profile.objects.all()
	return render(request, "core/table.html", {"users":user_list})