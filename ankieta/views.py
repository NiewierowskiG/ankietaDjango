from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


def update_ankieta(request, id):
    context = {}
    obj = get_object_or_404(Ankieta, id=id)
    form = AnkietaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/ankieta/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "ankieta/update.html", context)
