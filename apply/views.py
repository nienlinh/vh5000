from django.contrib.auth import login
from django.shortcuts import render
from .models import Person
from .forms import PersonModelForm
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def welcome(request):
    if request.user.is_authenticated:
        return redirect("/apply/myapply")
    else:    
        return render(request, "apply/welcome.html")

# you can apply only when you have login
'''
if POST
    if applied person
       f = form(POST, applied person)   # update
       save if valid; show fail if invalid
    else                                # create new
       f = form(POST)
       save if valid; show fail if invalid
else (GET)
    if applied person
       f = form(applied person)
       go to apply
    else
       f = new form
       go to apply
'''
@login_required
def apply(request):
    if request.method == "POST":
        applied_person = Person.objects.filter(account = request.user)
        if applied_person: 
            update_person = applied_person[0]
            form = PersonModelForm(request.POST, instance = update_person)
            if form.is_valid():
                form.save()
                return render(request, "apply/apply_success.html", {'form': form}) 
            else: 
                return render(request, "apply/apply_fail.html", {'form': form}) 
        else:
            form = PersonModelForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.account = request.user
                model_instance.save()
                return render(request, "apply/apply_success.html", {'form': form}) 
            else:
                return render(request, "apply/apply_fail.html", {'form': form}) 
    
    # GET
    applied_person = Person.objects.filter(account = request.user)
    if applied_person: 
        form = PersonModelForm(instance = applied_person[0])
    else:
        form = PersonModelForm()

    return render(request, "apply/apply.html", {'form': form})

# show my application data based on the login account
@login_required
def myapply(request):
    context = {}
    if request.user.is_authenticated:
        # get the person
        person = Person.objects.filter(account=request.user)
        if person:
            context = {
                "user": request.user,
                "person": person[0]
            }
        return render(request, "apply/my_apply.html", context)
    else:
        return redirect("/accounts/login")           


# show application for all persons
def show_all_apply(request):
    person_list = Person.objects.all()
    context = {
        'person_list': person_list
    }
    return render(request, "apply/show_all.html", context)

from django.shortcuts import get_object_or_404

# update the data based on the person's primay key
def update_apply(request, id):
    obj = get_object_or_404(Person, id = id)
    # obj = Person.objects.get(id = id)
    form = PersonModelForm(request.POST or None, instance = obj)

    print (">> form.is_bound: ", form.is_bound)
    print (">> form.is_valid(): ", form.is_valid())
    print (">> When form is not bound, it is not valid")
    if form.is_valid():
        form.save()
        return render(request, "apply/update_success.html")
 
    context = {'form':form} 
 
    return render(request, "apply/update_apply.html", context)
