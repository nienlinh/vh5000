from register.models import Person
from random import choice, randint 

print (Person.objects.all())

def gen_ssn():
    f = 'a b c d e f g h s m'.split()
    r = choice(f)
    for i in range(9):
        r = r + str(randint(0,9))
    print (r) 
    return (r)   

def gen_tel():
    tel = '09'
    for i in range(8):
        tel = tel + str(randint(0,9))
    print (tel)
    return (tel)    

def gen_vh():
    VOUCHER_CHOICES = [
        ('PP', '紙本'),
        ('CC', '信用卡'),
        ('ET', '電子票劵'),
        ('MB', '行動支付')]
    r = choice(VOUCHER_CHOICES)[0]
    print(r)
    return (r)

for p in range(10):
    _ssn = gen_ssn()
    _tel = gen_tel()
    _vh = gen_vh()
    # print (_ssn, _tel, _vh)
    person = Person.objects.create(
        ssn = _ssn,
        tel = _tel,
        voucher_id = _vh)
    person.save()    
