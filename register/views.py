from django.shortcuts import render,redirect
from .models import Person, Voucher
from .forms import PersonModelForm
# Create your views here.

def index(request):
    form = PersonModelForm()

    if request.method == "POST":
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form_id = form.save()
            message = {'choice': form.cleaned_data['voucher_id'],
                       'id': form_id.id}
            print(form.cleaned_data['voucher_id'])
        return render(request, "register/result.html", message)

    context = {
        'form': form
    }

    return render(request, "register/index.html", context)

def update(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonModelForm(instance=person)

    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            form_id = form.save()
            message = {'choice': form.cleaned_data['voucher_id'],
                       'id': form_id.id}
            print(form.cleaned_data['voucher_id'])
        return render(request, "register/result.html", message)

    context = {
        'form': form
    }

    return render(request, "register/update.html", context)