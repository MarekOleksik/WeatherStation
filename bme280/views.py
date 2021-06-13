from django.shortcuts import render,redirect
from bme280.models import Bme280
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


def dataTable(request):
    readings = Bme280.objects.all()
    return render(request, "bme280/dataTable.html", {
        "reading": readings
        })           

def bme280(request):
    return render(request, "bme280/index.html")

def index(request):
    return render(request, "bme280/index.html")

class DataFromBase():

    def getTemperature():
        readings = Bme280.objects.all()
        temperature = []
        for read in readings:
            temperature.append(read.temperature)
        return temperature

    def getHumidity():
        readings = Bme280.objects.all()
        humidity = []
        for read in readings:
            humidity.append(read.humidity)
        return humidity

    def getPressure():
        readings = Bme280.objects.all()
        pressure = []
        for read in readings:
            pressure.append(read.pressure)
        return pressure

    def getDate():
        readings = Bme280.objects.all()
        date = []
        for read in readings:
            date.append(str ((read.date).day) + "." + str ((read.date).month) + "-" + str ((read.date).hour) 
            + ":" + str ((read.date).minute)) 
        return date

class LineChartJSONTempView(BaseLineChartView):
    def get_labels(self):
        return DataFromBase.getDate()

    def get_providers(self):
        return ["Temperature"]

    def get_data(self):
        return [DataFromBase.getTemperature()]


class LineChartJSONHumidityView(BaseLineChartView):
    def get_labels(self):
        return DataFromBase.getDate()

    def get_providers(self):
        return ["Humidity"]

    def get_data(self):
        return [DataFromBase.getHumidity()]

class LineChartJSONPressureView(BaseLineChartView):
    def get_labels(self):
        return DataFromBase.getDate()

    def get_providers(self):
        return ["Pressure"]

    def get_data(self):
        return [DataFromBase.getPressure()]


line_chart_temp = TemplateView.as_view(template_name='bme280/chartTemp.html')
line_chart_json_temp = LineChartJSONTempView.as_view()    
line_chart_humidity = TemplateView.as_view(template_name='bme280/chartHumidity.html')
line_chart_json_humidity = LineChartJSONHumidityView.as_view() 
line_chart_pressure = TemplateView.as_view(template_name='bme280/chartPressure.html')
line_chart_json_pressure = LineChartJSONPressureView.as_view() 
    