from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='variableList'),
    path('get_by_id/<int:key_id>', views.get_measurement,name='dar_variable_por_id'),
    path('delete_by_id/<int:key_id>', views.delete_measurement,name= 'eliminar_variable_por_id' ),
    path('update_by_id/<int:key_id>/<int:measurement_value>', views.update_measurement_value, name='eliminar_variable_por_id'),
]