from django.shortcuts import render,HttpResponse

# Create your views here.
def fest_home(request):
    return HttpResponse("<h1>this is fest app page</h1>")
def about(request):
    return HttpResponse("<h1>this is about app page</h1>")
    