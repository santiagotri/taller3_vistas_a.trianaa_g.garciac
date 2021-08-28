from .logic.logic_measurements import *
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse (measurements_list, content_type='application/json')

def get_measurement(request, key_id=1):
    measurement = get_measurement_by_id(key_id)
    measurements = [measurement]
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse (measurements_list, content_type='application/json')

def delete_measurement(request, key_id=1):
    delete_measurement_by_id(key_id)
    return HttpResponse("Eliminado con exito measurement con id:" + str(key_id))

def update_measurement_value(requesy, key_id=1, measurement_value=0):
    measurement = update_measurement_value_by_id(key_id, measurement_value)
    measurements = [measurement]
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')
# Acá lo que está haciendo es convertir  la información de cada uno de los
# Objetos en un formato JSON