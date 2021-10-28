from django.http import HttpResponse
from django.shortcuts import render

def women_index(request):
    return HttpResponse("Приложение Woman")

def women_cats(request):
    return HttpResponse("<h1>Женские статьи по категориям</h1>")