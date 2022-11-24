from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse

from base.forms import ContactForm


def index(request):
    return render(request, 'base/index.html')

def uslugi(request):
    return render(request, 'base/uslugi.html')

def price(request):
    return render(request, 'base/price.html')

def about(request):
    return render(request, 'base/about.html')

def thanks(request):
    return render(request, 'base/thanks.html')

def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                'name': form.cleaned_data['name'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = f'Имя {body["name"]} Телефон {body["phone"]} Доп. информация{body["message"]}'
            context = {'success': 1}
            send_message(message)
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, "base/contacts.html", context=context)

def send_message(message):
    send_mail(subject='Заявка с сайта', message= message, from_email= 'chipkazan116@yandex.ru', recipient_list = ['chipkazan116@yandex.ru'])


