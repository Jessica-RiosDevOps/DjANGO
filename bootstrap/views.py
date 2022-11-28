from django.views.generic import TemplateView 
#from django.shortcuts import render
    
# Create your views here.
class TemplateView(TemplateView):
    template_name = "index.html"

