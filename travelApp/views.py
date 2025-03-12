from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Hyderabad'
    dest1.desc = 'City of Pearls'
    dest1.img = 'hydcharminar.jpeg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Mumbai'
    dest2.desc = 'City that never sleeps'
    dest2.img = 'mumbaitaj.jpg'
    dest2.price = 650
    dest1.offer = True

    dest3 = Destination()
    dest3.name = 'Goa'
    dest3.desc = 'City of Beaches'
    dest3.img = 'goa.jpg'
    dest3.price = 850
    dest1.offer = True

    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests': dests})
