from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Sightings
from django.template import loader

import datetime

def _map(request):
    sightings = Sightings.objects.all()[:30]
    template = loader.get_template('sightings/map.html')
    context = {
        'sightings': sightings,
    }
    return HttpResponse(template.render(context, request))

def stats(request):
    num = Sightings.objects.all().count()
    
    adult = Sightings.objects.filter(Age='Adult').count()
    juvenile = Sightings.objects.filter(Age='Juvenile').count()
    age_no_data = num - adult - juvenile
    
    adult_rate = adult / num
    juvenile_rate = juvenile / num
    age_no_data_rate = age_no_data / num
    
    Gray = Sightings.objects.filter(Primary_Fur_Color='Gray').count()
    Cinnamon = Sightings.objects.filter(Primary_Fur_Color='Cinnamon').count()
    Black = Sightings.objects.filter(Primary_Fur_Color='Black').count()
    fur_no_data = num - Gray - Cinnamon - Black
    Gray_rate = Gray / num
    Cinnamon_rate = Cinnamon / num
    Black_rate = Black / num
    fur_no_data_rate = fur_no_data / num
    
    Ground_Plane = Sightings.objects.filter(Location='Ground Plane').count()
    Above_Ground = Sightings.objects.filter(Location='Above Ground').count()
    Location_no_data = num - Ground_Plane - Above_Ground
    Ground_Plane_rate = Ground_Plane / num
    Above_Ground_rate = Above_Ground / num
    Location_no_data_rate = Location_no_data / num
    
    AM = Sightings.objects.filter(Shift='AM').count()
    PM = Sightings.objects.filter(Shift='PM').count()
    AM_rate = AM / num
    PM_rate = PM / num
    
    t = Sightings.objects.filter(Indifferent=True).count()
    f = Sightings.objects.filter(Indifferent=False).count()
    t_rate = t / num
    f_rate = f / num
    
    template = loader.get_template('sightings/stats.html')
    context = {
        'adult' : adult,
        'juvenile' : juvenile,
        'age_no_data' : age_no_data,
        'adult_rate' : adult_rate,
        'juvenile_rate' : juvenile_rate,
        'age_no_data_rate' : age_no_data_rate,
        'Gray' : Gray,
        'Cinnamon' : Cinnamon,
        'Black' : Black,
        'fur_no_data' : fur_no_data,
        'Gray_rate' : Gray_rate,
        'Cinnamon_rate' : Cinnamon_rate,
        'Black_rate' : Black_rate,
        'fur_no_data_rate' : fur_no_data_rate,
        'Ground_Plane' : Ground_Plane,
        'Above_Ground' : Above_Ground,
        'Location_no_data' : Location_no_data,
        'Ground_Plane_rate' : Ground_Plane_rate,
        'Above_Ground_rate' : Above_Ground_rate,
        'Location_no_data_rate' : Location_no_data_rate,
        'AM' : AM,
        'PM' : PM,
        'AM_rate' : AM_rate,
        'PM_rate' : PM_rate,
        't' : t,
        'f' : f,
        't_rate' : t_rate,
        'f_rate' : f_rate,
    }
    return HttpResponse(template.render(context, request))

def sightings_list(request):
    the_list = Sightings.objects.all()
    template = loader.get_template('sightings/sightings_list.html')
    context = {
        'the_list': the_list,
    }
    return HttpResponse(template.render(context, request))

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