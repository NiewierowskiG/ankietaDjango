from django.shortcuts import render
from .models import Ankieta


def list_view(request):
    context = {
        'data': Ankieta.objects.all()
    }
    return render(request, 'ankieta/list.html', context)
