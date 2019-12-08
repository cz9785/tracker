from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv

class Command(BaseCommand):
    help = 'export data'

    def add_arguments(self, parser):
        parser.add_argument('filepath')

    def handle(self, *args, **options):
        if options['filepath']:
            filepath = options['filepath']
        else:
            raise CommandError("no file path!")
        data = Sightings.objects.values_list()
        label = ['','Latitude','Longitude','Unique Squirrel ID',
                 'Shift','Date','Age','Primary Fur Color',
                 'Location','Specific Location','Running',
                 'Chasing','Climbing','Eating','Foraging',
                 'Other Activities','Kuks','Quaas','Moans',
                 'Tail flags','Tail twitches','Approaches',
                 'Indifferent','Runs from']
        with open(filepath, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(label)
            writer.writerows(data)