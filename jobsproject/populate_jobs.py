import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
fake=Faker()
from random import *

def phonenumbergen():
    d1=randint(7,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','BCA'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        # hydjobs_record=hydjobs.objects.get_or_create(date=fdate,
        # company=fcompany,title=ftitle,eligibility=feligibility,
        # address=faddress,email=femail,phonenumber=fphonenumber)

        # blorejobs_record=blorejobs.objects.get_or_create(date=fdate,
        # company=fcompany,title=ftitle,eligibility=feligibility,
        # address=faddress,email=femail,phonenumber=fphonenumber)

        # chennaijobs_record=chennaijobs.objects.get_or_create(date=fdate,
        # company=fcompany,title=ftitle,eligibility=feligibility,
        # address=faddress,email=femail,phonenumber=fphonenumber)

        punejobs_record=punejobs.objects.get_or_create(date=fdate,
        company=fcompany,title=ftitle,eligibility=feligibility,
        address=faddress,email=femail,phonenumber=fphonenumber)


populate(20)
