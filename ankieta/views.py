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
        return HttpResponseRedirect("/ankieta/")
    context['form'] = form
    return render(request, "ankieta/create.html", context)


def update_ankieta(request, id):
    context = {}
    obj = get_object_or_404(Ankieta, id=id)
    form = AnkietaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/ankieta/")

    context["form"] = form
    return render(request, "ankieta/update.html", context)


def delete_ankieta(request, id):
    obj = get_object_or_404(Ankieta, id=id)
    obj.delete()
    return HttpResponseRedirect("/ankieta/")


def single_ankieta(request, id):
    context = {}
    obj = get_object_or_404(Ankieta, id=id)
    context["obj"] = obj
    return render(request, "ankieta/single.html", context)
