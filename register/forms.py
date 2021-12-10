from django import forms
from .models import Person


class PersonModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'  # 顯示Model中所有欄位
        widgets = {
            'ssn': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'voucher_id': forms.RadioSelect()
        }
        labels = {
            'ssn': '身分證字號',
            'tel': '電話號碼',
            'voucher_id': '綁定'
        }