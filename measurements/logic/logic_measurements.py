from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_by_id(id:int):
    measurement = Measurement.objects.get(pk=id)
    return measurement

def delete_measurement_by_id(id:int):
    measurement = get_measurement_by_id(id)
    measurement.delete()

def update_measurement_value_by_id(id:int, measurement_value:int):
    measurement = get_measurement_by_id(id)
    measurement.value =measurement_value
    measurement.save()
    return measurement












