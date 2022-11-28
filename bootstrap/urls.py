from os import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(), name="index.html"),
]