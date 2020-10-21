from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from yf import filterStocks



def hi(request):

    zipped = filterStocks()
    return render(request, 'stockApp/main.html',
                  context={"zipped" : zipped})
