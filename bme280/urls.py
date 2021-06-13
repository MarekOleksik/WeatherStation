from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("bme280", views.bme280, name="bme280"),
    path('dataTable',views.dataTable, name="dataTable"),
    path('chart/', views.chart, name='chart'),
]