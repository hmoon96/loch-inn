from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    """
    
    """
    template_name = 'jukebox/index.html'


class MusicPage(TemplateView):
    """
    
    """
    template_name = 'jukebox/music.html'