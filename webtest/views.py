from django.http import *
import requests

def hi(request):
    return HttpResponse('Done.')

def bd(self):
    return HttpHeaders(self.META)