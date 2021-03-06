# Generated by Django 2.2.7 on 2019-12-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(help_text='Latitude')),
                ('Longitude', models.FloatField(help_text='Longitude')),
                ('Unique_Squirrel_Id', models.CharField(help_text='Unique Squirrel ID', max_length=16)),
                ('Shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], default='AM', max_length=2)),
                ('Date', models.DateField(help_text='Date')),
                ('Age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('other', 'Other')], default='other', max_length=20)),
                ('Primary_Fur_Color', models.CharField(choices=[('gray', 'Gray'), ('cinnamon', 'Cinnamon'), ('black', 'Black'), ('other', 'Other')], default='other', help_text='Primary Fur Color', max_length=20)),
                ('Location', models.CharField(choices=[('ground plane', 'Ground Plane'), ('above ground', 'Above Ground'), ('other', 'Other')], default='other', max_length=50)),
                ('Specific_Location', models.CharField(help_text='Specific location', max_length=1000, null=True)),
                ('Running', models.NullBooleanField(help_text='Squirrel was seen running or not')),
                ('Chasing', models.NullBooleanField(help_text='Squirrel was seen chasing others or not')),
                ('Climbing', models.NullBooleanField(help_text='Squirrel was seen climbing a tree or not')),
                ('Eating', models.NullBooleanField(help_text='Squirrel was seen eating or not')),
                ('Foraging', models.NullBooleanField(help_text='Squirrel was seen foraging for food or not')),
                ('Other_Activities', models.CharField(help_text='Other behaviors of squirrels', max_length=128, null=True)),
                ('Kuks', models.NullBooleanField(help_text='Squirrel was heard kukking or not (a chirpy vocal communication)')),
                ('Quaas', models.NullBooleanField(help_text='Squirrel was heard Quaaing or not (an elongated vocal communication)')),
                ('Moans', models.NullBooleanField(help_text='Squirrel was heard Moaning or not (a high-pitched vocal communication)')),
                ('Tail_flags', models.NullBooleanField(help_text='Squirrel was seen flaging its tail or not')),
                ('Tail_twitches', models.NullBooleanField(help_text='Squirrel was seen twitching its tail or not')),
                ('Approaches', models.NullBooleanField(help_text='Squirrel was seen approaching human or not')),
                ('Indifferent', models.NullBooleanField(help_text='Squirrel was indifferent to human presence or not')),
                ('Runs_from', models.NullBooleanField(help_text='Squirrel was seen running from humans or not')),
            ],
        ),
    ]
