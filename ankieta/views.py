from django.shortcuts import render
from .models import Ankieta
from .forms import AnkietaForm


def list_view(request):
    context = {
        'data': Ankieta.objects.all()
    }
    return render(request, 'ankieta/list.html', context)


def create_ankieta(request):
    context = {}
    form = AnkietaForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "ankieta/create.html", context)
