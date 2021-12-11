from django.shortcuts import render
from .models import Person, Voucher
from .forms import PersonModelForm
from django.http import HttpResponse


def index(request):

    if request.method == "POST":
        # save to DB
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            # re-direct to a html (show success information)
            context = {'form': form}
            return render(request, "register/apply_success.html", context)            

    else:
        # GET, show the empty from to fill
        form = PersonModelForm()

    context = {
        'form': form
    }

    # field the form
    return render(request, "register/apply1.html", context)