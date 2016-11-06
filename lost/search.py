from django.db import models

from models import Data

def print_searchtag():
    for b in Data.objects.all().filter(name='Priyank'): 
        print b