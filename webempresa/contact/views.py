from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
import sys

# Create your views here.
def contact(request):
    #print("Tipo de petición = {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        #Se rellena el formulario con los mismos datos. 
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Se envía el correo 
            email = EmailMessage(
                    "La caftiera: Nuevo mensaje de contacto", 
                    "De {} <{}> \n\n Escribió: \n\n{}".format(name, email, content),
                    "no-contestar@inbox.mailtrap.io",
                    ['franvazgom@gmail.com',],
                    reply_to=[email]
            )
            try:
                email.send()
                #Se redirecciona la página
                return redirect(reverse('contact')+"?ok")
            except:
                print("Unexpected error: ", sys.exc_info()[0])
                return redirect(reverse('contact')+"?fail")
    return render(request, 'contact/contact.html', {'form':contact_form})
