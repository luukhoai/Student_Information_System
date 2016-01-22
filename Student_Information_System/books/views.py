from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher