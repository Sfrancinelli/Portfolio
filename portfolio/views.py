from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
from projects.models import Contact
from projects.forms import ContactForm


def index(request):
    return render(request, 'pages/index.html', {'title': 'Title'})


def about(request):
    return render(request, 'pages/about.html', {'title': 'Información'})


def contact(request):
    if request.method = 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            mensaje = form.cleaned_data['message']

            if company == '':
                company = 'Sin especificar'
            else:

                form.save()

                subject = f'Contacto de {name} de la empresa {company}'
                message = f'La persona {name} de la empresa {company} ha enviado un mensaje de contacto:\n{mensaje}\nPara responder este mensaje comuniquese vía: {email}'
                from_email = 'programacion101200@gmail.com'
                recipient_list = ['seebaapa@gmail.com']
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                messages.success(request, 'Gracias por contactarme! Te estaré respondiendo en la brevedad!')

                return redirect('index')

        else:
                print(form.errors)
    else:
        context = {'form': form}
        return render(request, 'pages/contact.html', context)
    else:
        form = ContactForm()
        conext = {'form': form}

        return render(request, 'pages/contact.html', context)
            

    return render(request, 'pages/contact.html', context)
