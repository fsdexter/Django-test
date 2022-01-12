from django.shortcuts import render

# Create your views here.


def greeting(request):
    name = "Guido van Rossum"
    return render(request, "index.html", {"name": name})