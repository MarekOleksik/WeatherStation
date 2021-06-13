from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("bme280", views.bme280, name="bme280"),
    path('dataTable',views.dataTable, name="dataTable"),
    path('chartTemp', views.line_chart_temp, name='line_chart_temp'),
    path('chartJSONTemp', views.line_chart_json_temp, name='line_chart_json_temp'),
    path('chartHumidity', views.line_chart_humidity, name='line_chart_humidity'),
    path('chartJSONHumidity', views.line_chart_json_humidity, name='line_chart_json_humidity'),
    path('chartPressure', views.line_chart_pressure, name='line_chart_pressure'),
    path('chartJSONPressure', views.line_chart_json_pressure, name='line_chart_json_pressure'),
]