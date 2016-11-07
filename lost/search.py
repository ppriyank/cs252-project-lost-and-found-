from django.db import models

from models import Data

def print_searchtag():
    for b in Data.tags.all().filter(Tag='Red'): 
        print b