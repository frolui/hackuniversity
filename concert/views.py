from django.http import HttpResponse
from django.shortcuts import render
import sys
from django.db import models
from concert.models import Sounds
from django.core import serializers
from django.http import HttpResponse

sys.path.append('/home/frolui/bty/')

def index(request):
    return json(request)

def json(request):
    id_sounds = request.GET.get('id_sounds', '')
    sound = Sounds.objects.filter(id = id_sounds)
    qs_json = serializers.serialize('json', sound)
    return HttpResponse(qs_json, content_type='application/json')


