
# please type 'python manage.py shell' to do the follow experiments.

from apply.forms import PersonModelForm

f = PersonModelForm()
print (f)

f.as_table()

f.as_p()

f.as_ul()

f.is_bound      # will return False

f = PersonModelForm({'ssn':'a123456789','tel':'0912-901-109','voucher_id':'PP'})

f.is_bound      # will return True

f.is_valid()    # will return True

f = PersonModelForm({'ssn':'a123456789','tel':'0912','voucher_id':'PP'})

f.is_valid()    # will return False

f.errors        # {'tel': ['Invalid Tel']}

f.cleaned_data  # will return {'ssn': 'a123456789', 'voucher_id': 'PP'}