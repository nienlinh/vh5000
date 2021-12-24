from django.contrib.auth import login
from django.shortcuts import render
from .models import Person
from .forms import PersonModelForm
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def welcome(request):
    return render(request, "apply/welcome.html")

# you can apply only when you have login
@login_required
def apply(request):
    if request.method == "POST":
        # save to DB
        form = PersonModelForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.account = request.user
            model_instance.save()
            # re-direct to a html (show success information)
            return render(request, "apply/apply_success.html", context) 
        else:
            return render(request, "apply/apply_fail.html", context) 
    
    form = PersonModelForm()

    context = {
        'form': form
    }

    # field the form
    return render(request, "apply/apply.html", context)

# show my application data based on the login account
@login_required
def myapply(request):
    pass_auth = False
    if request.user.is_authenticated:
        pass_auth = True
        # get the person
        person = Person.objects.filter(account=request.user)[0]
    else:
        print ("not authenticated") 
           
    context = {
        "pass_auth": pass_auth, 
        "user": request.user,
        "person": person 
    }
    return render(request, "apply/my_apply.html", context)


# show application for all persons
def show_all_apply(request):
    person_list = Person.objects.all()
    context = {
        'person_list': person_list
    }
    return render(request, "apply/show.html", context)




# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import DetailView

