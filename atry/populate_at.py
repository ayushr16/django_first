import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','atry.settings')
import django
django.setup()

from at.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        em = fakegen.email()
        ph = fakegen.phone_number()
        fir = fakegen.first_name()
        las = fakegen.last_name()

        use = User.objects.get_or_create(email=em,phone = ph,firstname=fir,surname=las)[0]

if __name__ == '__main__':
    print("Started populating the data")
    populate(25)
