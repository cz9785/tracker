from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Sightings
from django.template import loader

import datetime


def Update(request,Unique_Squirrel_Id):
    squirrel=Sightings.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    print(request.method)
    if request.method == 'POST':
        squirrel.Latitude=request.POST.get('Latitude',None)
        squirrel.Longitude=request.POST.get('Longitude',None)
        squirrel.Unique_Squirrel_Id=request.POST.get('Unique_Squirrel_Id',None)
        squirrel.Shift=request.POST.get('Shift',None)
        date_str=[int(s) for s in request.POST.get('Date',None).split('-')]
        squirrel.Date=datetime.date(date_str[0],date_str[1],date_str[2])
        squirrel.Age=request.POST.get('Age',None)
        squirrel.Primary_Fur_Color=request.POST.get('Primary_Fur_Color',None)
        squirrel.Location=request.POST.get('Location',None)
        squirrel.Specific_Location=request.POST.get('Specific_Location',None)
        squirrel.Running=request.POST.get('Running',None)
        squirrel.Chasing=request.POST.get('Chasing',None)
        squirrel.Climbing=request.POST.get('Climbing',None)
        squirrel.Eating=request.POST.get('Eating',None)
        squirrel.Foraging=request.POST.get('Foraging',None)
        squirrel.Other_Activities=request.POST.get('Other_Activities',None)
        squirrel.Kuks=request.POST.get('Kuks',None)
        squirrel.Quaas=request.POST.get('Quaas',None)
        squirrel.Moans=request.POST.get('Moans',None)
        squirrel.Tail_flags=request.POST.get('Tail_flags',None)
        squirrel.Tail_twitches=request.POST.get('Tail_twitches',None)
        squirrel.Approaches=request.POST.get('Approaches',None)
        squirrel.Indifferent=request.POST.get('Indifferent',None)
        squirrel.Runs_from=request.POST.get('Runs_from',None)

        squirrel.save()
    return render(request,'sightings/squirrel.html',{'squirrel':squirrel})
    pass




def Add(request):
    
    try:
        Latitude=request.POST['Latitude']
        Longitude=request.POST['Longitude']
        Unique_Squirrel_Id=request.POST['Unique_Squirrel_Id']
        Shift=request.POST['Shift']
        Date=request.POST['Date']
        Age=request.POST['Age']
        Primary_Fur_Color=request.POST['Primary_Fur_Color']
        Location=request.POST['Location']
        Specific_Location=request.POST['Specific_Location']
        Running=request.POST['Running']
        Chasing=request.POST['Chasing']
        Climbing=request.POST['Climbing']
        Eating=request.POST['Eating']
        Foraging=request.POST['Foraging']
        Other_Activities=request.POST['Other_Activities']
        Kuks=request.POST['Kuks']
        Quaas=request.POST['Quaas']
        Moans=request.POST['Moans']
        Tail_flags=request.POST['Tail_flags']
        Tail_twitches=request.POST['Tail_twitches']
        Approaches=request.POST['Approaches']
        Indifferent=request.POST['Indifferent']
        Runs_from=request.POST['Runs_from']
        
        Sightings.objects.create(
                        Latitude=Latitude,
                        Longitude=Longitude,
                        Unique_Squirrel_Id=Unique_Squirrel_Id,
                        Shift=Shift,
                        Date=Date,
                        Age=Age,
                        Primary_Fur_Color=Primary_Fur_Color,
                        Location=Location,
                        Specific_Location=Specific_Location,
                        Running=Running,
                        Chasing=Chasing,
                        Climbing=Climbing,
                        Eating=Eating,
                        Foraging=Foraging,
                        Other_Activities=Other_Activities,
                        Kuks=Kuks,
                        Quaas=Quaas,
                        Moans=Moans,
                        Tail_flags=Tail_flags,
                        Tail_twitches=Tail_twitches,
                        Approaches=Approaches,
                        Indifferent=Indifferent,
                        Runs_from=Runs_from,)
                        

    except Exception as e:
        print(e)
    return render(request,'sightings/add.html',)