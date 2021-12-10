from django.shortcuts import render
from .models import Person, Voucher
from .forms import PersonModelForm
# Create your views here.

def index(request):
    form = PersonModelForm()
    context = {
        'form': form
    }

    return render(request, "register/apply.html", context)