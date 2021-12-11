from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class PersonModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'  # __all__ 表示要全部呈現中所有欄位

        labels = {
            'ssn': '身分證字號',
            'tel': '電話號碼',
            'voucher_id': '綁定'
        }
