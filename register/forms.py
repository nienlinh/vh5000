from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class PersonModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'  # __all__ 表示要全部呈現中所有欄位
        # fields = ['ssn', 'tel', 'voucher_id'] # 可以用 list 列出要呈現的欄位

        # widget 用來設定介面的呈現
        widgets = {
            # html 的 class 為 form-control
            'ssn': forms.TextInput(attrs = {'class': 'form-control'}),
            'tel': forms.TextInput(attrs = {'class': 'form-control'}),
            # 'voucher_id': forms.RadioSelect()
            'voucher_id': forms.Select(attrs = {'class': 'form-control'}),
        }

        labels = {
            'ssn': '身分證字號',
            'tel': '電話號碼',
            'voucher_id': '綁定'
        }

   # override the clean_<fieldname>() method
    def clean_ssn(self):
        data = self.cleaned_data['ssn']

        if len(data) != 10 :
            # raise ValidationError('Invalid SSN')
            print ('SSN error, len must be 10')

        # Remember to always return the cleaned data.
        return data