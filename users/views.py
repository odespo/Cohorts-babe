from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users.models import *
import json

# Create your views here.

def createUser(request):
    try:
        user_number = request.POST.get('user_number', False)
        user_name = request.POST.get('user_name', False)

        if not user_number or not user_name:
            return HttpResponse(0)

        p = Person(phone_number=str(user_number), name=str(user_name))
        p.save()
        # TODO: what to return?
        return HttpResponse(1)
    except:
        return HttpResponse(0)

def createRating(request):
    rater_number = request.POST.get('rater_number', False)
    rated_number = request.POST.get('rated_number', False)
    ratings = request.POST.get('ratings', False)
    
    if not rater_number or not rated_number or not ratings:
        return HttpResponse(0)

    if rater_number == rated_number:
        return HttpResponse(0)
    try:
        rater = Person.objects.get(phone_number = str(rater_number))
        rated = Person.objects.get(phone_number = str(rated_number))
        rating_dump = json.dumps(ratings)
        rating = Rating(person_rating = rater, person_rated = rated, rating_list=rating_dump)
        rating.save()
        return HttpResponse(1)
    except:
        return HttpResponse(0)
