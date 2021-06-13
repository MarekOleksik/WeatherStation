from django.shortcuts import render,redirect
from bme280.models import Bme280


def dataTable(request):
    readings = Bme280.objects.all()
    return render(request, "bme280/dataTable.html", {
        "reading": readings
        })

def chart(request):
    readings = Bme280.objects.all()
    labels = []
    dataTemperature = []
    dataPressure = []
    dataHumidity = []
    for read in readings:
        labels.append(read.date)
        dataTemperature.append(read.temperature)
        dataPressure.append(read.pressure)
        dataHumidity.append(read.humidity)
    return render(request, "bme280/chart.html", {
        "labels": labels, "dataTemperature": dataTemperature, 
        "dataPressure": dataPressure, "dataHumidity": dataHumidity
        })                  

def bme280(request):
    return render(request, "bme280/index.html")

def index(request):
    return render(request, "bme280/index.html")

    
    