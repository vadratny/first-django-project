from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse()

def home_page(request):
    f = open('C:\\Users\\David\\Desktop\\django\\coolsite\\page\\pages\\list_1.html', 'rb')
    return HttpResponse(f.read())
def man_1_page(request):
    f = open('C:\\Users\\David\\Desktop\\django\\coolsite\\page\\pages\\man_1.html', 'rb')
    return HttpResponse(f.read())
def man_2_page(request):
    f = open('C:\\Users\\David\\Desktop\\django\\coolsite\\page\\pages\\man_2.html', 'rb')
    return HttpResponse(f.read())
def man_3_page(request):
    f = open('C:\\Users\\David\\Desktop\\django\\coolsite\\page\\pages\\man_3.html', 'rb')
    return HttpResponse(f.read())
def man_4_page(request):
    f = open('C:\\Users\\David\\Desktop\\django\\coolsite\\page\\pages\\man_4.html', 'rb')
    return HttpResponse(f.read())