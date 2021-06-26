from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    name = ["Илья", "Саша", "Дима"]
    return render(request, "blog/index.html", context={"names":name})