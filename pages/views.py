from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def my_first_view(request):
    return render(request, 'base.html')

def about_view(request):
    return render(request, 'pages/about_me.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Valid Form")
            
            #Clean Data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            message_body = render_to_string('content/email.html', request.POST)
            
            # Send Email
            send_mail(
                "Portfolio Email",
                message,
                email,
                ['savagedamian99@gmail.com'],
                html_message=message_body,
            )
            
        else:
            print("Invalid Form")
            
    else:
        form = ContactForm()
        
    return render(request, 'pages/contact.html', {'form': form})

