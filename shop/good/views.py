from django.shortcuts import render
from . import models

def main(request, uprice):
    context = {
        'good': models.Good.objects.filter(price = uprice),
        'uprice': uprice
    }
    return render(
        request,
        'good/index.html',
        context      
    )
