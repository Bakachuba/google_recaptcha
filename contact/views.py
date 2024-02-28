from django.http import HttpResponse
from django.shortcuts import render

from contact.forms import ContactForm


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return HttpResponse('Yay!')
        else:
            return HttpResponse('OOPS!')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})