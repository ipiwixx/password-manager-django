from django.shortcuts import render
from .models import Site

# Create your views here.
def site_list(request):
    sites = Site.objects.all()
    return render(request, 'passwordManager/site_list.html', {'sites':sites})