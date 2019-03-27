import os
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    files = os.listdir(os.path.join('pictures/static/pictures/pix'))
    context = {
        'files': files
    }
    return render(request, 'pictures/index.html', context)
