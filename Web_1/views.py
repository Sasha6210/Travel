from django.shortcuts import render
from .models import Customer, Category, Course
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, UserRegistrationForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    course = Course.objects.all()[:3]
    context = {'courses': course}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact_us(request):
    context = {'form': ContactForm}
    customers = Customer()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['text'], form.cleaned_data['phone'])
            customers.name = request.POST.get("name")
            customers.email = request.POST.get("email")
            customers.phone = request.POST.get("phone")
            customers.message = request.POST.get("text")
            customers.save()
            context = {'success': '1'}
    else:
        form = ContactForm()
    context["form"] = form
    return render(request, "contact-us.html", context)

def send_message(name, email, message, phone):
    text_send = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message, 'phone': phone}
    subject = 'Повідомлення із сайту'
    from_email = 'support@kodim.ua'
    text_content = text_send.render(context)
    html_content = text_send.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['kodim.pervomaisk@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()



def course(request, id):
    description = Course.objects.get(id=id)
    context = {'course': description}
    return render(request, "course.html", context)

def coursess(request):
    coursess = Course.objects.all()
    return render(request, "coursess.html", {"coursess":coursess})

def new_message(request):
    client = Customer()
    client.name = request.POST.get("name")
    client.email = request.POST.get("email")
    client.phone = request.POST.get("phone")
    client.message = request.POST.get("message")
    client.save()
    return HttpResponse()




def profile(request):
    return render(request, 'registration/profile.html')

class Register(View):
    templat_name = 'registration/register.html'

    def get(self, request):
        return render(request, self.templat_name, {'form': UserRegistrationForm})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, self.templat_name, {'form': form})
        






































#        |          -----------------
#        |          |
#        |          |
#        |          |
#        |          |
#        -----------|------------|
#                   |            |
#                   |            |
#                   |            |
#                   |            |
#        ------------