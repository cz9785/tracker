from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
# Create your models here.

class Sightings(models.Model):
    Latitude = models.FloatField(
            help_text = _('Latitude'),
            )
    
    Longitude = models.FloatField(
            help_text = _('Longitude'),
            )
    
    Unique_Squirrel_Id = models.CharField(
            max_length=16,
            help_text = _('Unique Squirrel ID'),
            )
    
    PM = 'PM'
    AM = 'AM'
    
    SHIFT_CHOICES = (
        (PM,'PM'),
        (AM,'AM'),
    )
    
    Shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        default=AM,
    )
    
    Date =  models.DateField(
        help_text = _('Date'),
    )
    
    ADULT='adult'
    JUVENILE='juvenile'
    OTHER='other'
    
    age_field = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (OTHER,'Other'),
            )
    
    Age = models.CharField(
            max_length=20,
            choices=age_field,
            default=OTHER,
            )
   
    GRAY='gray'
    CINNAMON='cinnamon'
    BLACK='black'

    color_field = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black' ),
        (OTHER,'Other'),
    )
    
    Primary_Fur_Color = models.CharField(
        max_length=20,
        choices=color_field,
        default=OTHER,
        help_text = _('Primary Fur Color')
    )

    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    location_field = (
        (GROUND_PLANE,'Ground Plane'),
        (ABOVE_GROUND,'Above Ground'),
        (OTHER,'Other'),
    )
    
    Location =  models.CharField(
        max_length=50,
        choices=location_field,
        default=OTHER,
    )

    Specific_Location = models.CharField(
        max_length = 1000,
        null = True,
        help_text = _('Specific location'),
    )
    
    Running = models.NullBooleanField(
        help_text = _('Squirrel was seen running or not'),
    )
    
    Chasing = models.NullBooleanField(
        help_text = _('Squirrel was seen chasing others or not'),
    )
    
    Climbing = models.NullBooleanField(
        help_text = _('Squirrel was seen climbing a tree or not'),
    )
    
    Eating = models.NullBooleanField(
        help_text = _('Squirrel was seen eating or not'),
    )
    
    Foraging = models.NullBooleanField(
        help_text = _('Squirrel was seen foraging for food or not'),
    )
    
    Other_Activities = models.CharField(
        max_length = 128,
        null = True,
        help_text = _('Other behaviors of squirrels'),
    )
    
    Kuks = models.NullBooleanField(
        help_text = _('Squirrel was heard kukking or not (a chirpy vocal communication)'),
    )
    
    Quaas = models.NullBooleanField(
        help_text = _('Squirrel was heard Quaaing or not (an elongated vocal communication)'),
    )
    
    Moans = models.NullBooleanField(
        help_text = _('Squirrel was heard Moaning or not (a high-pitched vocal communication)'),
    )
    
    Tail_flags = models.NullBooleanField(
        help_text = _('Squirrel was seen flaging its tail or not'),
    )
    
    Tail_twitches = models.NullBooleanField(
        help_text = _('Squirrel was seen twitching its tail or not'),
    )
    
    Approaches = models.NullBooleanField(
        help_text = _('Squirrel was seen approaching human or not'),
    )
    
    Indifferent = models.NullBooleanField(
        help_text = _('Squirrel was indifferent to human presence or not'),
    )
    
    Runs_from = models.NullBooleanField(
        help_text = _('Squirrel was seen running from humans or not'),
    )
    

    def __str__(self):
        return self.Unique_Squirrel_Id
    
    
    
    
    
    
    
    
    
    
    