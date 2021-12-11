from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class PersonModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['ssn', 'tel', 'voucher_id'] 

        # widget 用來設定介面的呈現
        widgets = {
            'ssn': forms.TextInput(attrs = {'class': 'form-control'}),
            'tel': forms.TextInput(attrs = {'class': 'form-control'}),
            'voucher_id': forms.RadioSelect()
            # 'voucher_id': forms.Select(attrs = {'class': 'form-control'}),
        }

        labels = {
            'ssn': '身分證字號',
            'tel': '電話號碼',
            'voucher_id': '綁定'
        }

    # override the clean_<fieldname>() method
    # 身分證必須剛好 10 個字
    def clean_ssn(self):
        data = self.cleaned_data['ssn'] # 通過基本檢查乾淨資料

        if len(data) != 10 :
            raise ValidationError('身分證長度必須為 10')

        # Remember to always return the cleaned data.
        return data

    # 電話號碼必須大於五個字
    def clean_tel(self):
        data = self.cleaned_data['tel']

        if len(data) < 5 :
            raise ValidationError('電話長度不可小於5')

        # Remember to always return the cleaned data.
        return data        