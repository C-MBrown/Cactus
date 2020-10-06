from django.shortcuts import render


def index(request) :
    return render(request, 'frontend/index.html')

def contact(request) :
    return render(request, 'frontend/contact.html')