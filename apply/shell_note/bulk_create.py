'''
cd apply/shell_note/                                                         
exec(open("bulk_create.py").read())
'''

from apply.models import Person
from random import choice, randint 

def gen_ssn():
    f = 'a b c d e f g h s m'.split()
    r = choice(f)
    for i in range(9):
        r = r + str(randint(0,9))
    return (r)   

def gen_tel():
    tel = '09'
    for i in range(8):
        tel = tel + str(randint(0,9))
    return (tel)    

def gen_vh():
    VOUCHER_CHOICES = [
        ('PP', '紙本'),
        ('CC', '信用卡'),
        ('ET', '電子票劵'),
        ('MB', '行動支付')]
    r = choice(VOUCHER_CHOICES)[0]
    return (r)

for p in range(10):
    person = Person.objects.create(
        ssn = gen_ssn(), 
        tel = gen_tel(),
        voucher_id = gen_vh() )
    person.save()    
