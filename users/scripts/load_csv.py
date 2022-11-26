# python manage.py runscript load_csv

import csv
from ..models import UserQuery
from os import listdir

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

def run() :
    files = find_csv_filenames('./')
    
    UserQuery.objects.all().delete()

    for f in files:
        with open(f) as file : 
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                query = UserQuery(userID=row[0], timestamp=row[1], messageBody=row[2])
                query.save()
