from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv

class Command(BaseCommand):
    help = 'import data'

    def add_arguments(self, parser):
        parser.add_argument('filepath')

    def handle(self, *args, **options):
        if options['filepath']:
            filepath = options['filepath']
        else:
            raise CommandError("no file path!")
        number_of_data = 0
        with open(filepath, encoding = "utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                number_of_data += 1
                d = row['Date'][4:8]+'-'+row['Date'][0:2]+'-'+row['Date'][2:4]
                Sightings.objects.create(Latitude = row['X'],
                                         Longitude = row['Y'],
                                         Unique_Squirrel_Id = row['Unique Squirrel ID'],
                                         Shift = row['Shift'],
                                         Date = d,
                                         Age = row['Age'],
                                         Primary_Fur_Color = row['Primary Fur Color'],
                                         Location = row['Location'],
                                         Specific_Location = row['Specific Location'],
                                         Running = True if row['Running'].lower()=='true' else False,
                                         Chasing = True if row['Chasing'].lower()=='true' else False,
                                         Climbing = True if row['Climbing'].lower()=='true' else False,
                                         Eating = True if row['Eating'].lower()=='true' else False,
                                         Foraging = True if row['Foraging'].lower()=='true' else False,
                                         Other_Activities = row['Other Activities'],
                                         Kuks = True if row['Kuks'].lower()=='true' else False,
                                         Quaas = True if row['Quaas'].lower()=='true' else False,
                                         Moans = True if row['Moans'].lower()=='true' else False,
                                         Tail_flags = True if row['Tail flags'].lower()=='true' else False,
                                         Tail_twitches = True if row['Tail twitches'].lower()=='true' else False,
                                         Approaches = True if row['Approaches'].lower()=='true' else False,
                                         Indifferent = True if row['Indifferent'].lower()=='true' else False,
                                         Runs_from = True if row['Runs from'].lower()=='true' else False)
            self.stdout.write(f'number of data:{number_of_data}')