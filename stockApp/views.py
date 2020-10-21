from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from yf import ExtractStocksData


def hi(request):

    stockLabels, current, data_1d, data_7d, data_30d, data_12mo = ExtractStocksData()
    return render(request, 'stockApp/main.html',
                  context={"stockLabels" : stockLabels,
                           "current" : current,
                           "data_1d" : data_1d,
                           "data_7d" : data_7d,
                           "data_30d" : data_30d,
                           "data_12mo" : data_12mo,

                              })
