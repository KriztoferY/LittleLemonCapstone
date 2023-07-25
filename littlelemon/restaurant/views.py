from rest_framework import generics
from .serializers import MenuSerializer
from .models import Menu
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


# Create your views here. 

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
