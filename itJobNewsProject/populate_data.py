import os
import  django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','itJobNewsProject.settings')
django.setup()

from jobNewsApp.models import pubeJobs
from faker import Faker
from random import *

faker=Faker()

def generatePhoneNumber():
    num=str(randint(6,9))
    for i in range(0,9):
        num=num+str(randint(0,9))

    return num

def populate_data(num):
    for i in range(num):
        fdate=faker.date()
        fcompany=faker.company()
        ftitle=faker.random_element(elements=('Project Manager','Team Lead','Software Engineer'))
        feligibility=faker.random_element(elements=('B.Tech','M.Tech','BCA','MCA','B.Sc-IT','Ph.D'))
        faddress=faker.address()
        femail=faker.email()
        fphonenumber=generatePhoneNumber()

        punejobs_record=pubeJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)


populate_data(25)



