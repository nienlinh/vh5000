from django.shortcuts import render
from .models import Person
from .forms import PersonModelForm

def index(request):

    if request.method == "POST":
        # save to DB
        form = PersonModelForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
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

def show_apply(request):
    person_list = Person.objects.all()
    context = {
        'person_list': person_list
    }
    return render(request, "apply/show.html", context)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

class ShowApplyByUserListView(LoginRequiredMixin, DetailView):
    model = Person
    template_name ='apply/appy_by_user.html'

    # def get_queryset(self):
    #     return Person.objects.filter(account=self.request.user).filter(status__exact='o').order_by('due_back')
