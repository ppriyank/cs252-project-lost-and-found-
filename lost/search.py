from django.db import models

from models import Data

def print_searchtag():
    for b in Data.tags.similar_objects(): 
        print b.name