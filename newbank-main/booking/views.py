from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Booking

# Create your views here.
def index(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/index.html', {'bookings': bookings})

@login_required
def add(request):
    if request.method == 'POST':
        # Process the form data here
        reason = request.POST['reason']
        date = request.POST['date']
        time = request.POST['time']
        user = request.user
        booking = Booking(reason=reason, date=date, time=time, booked_by=user)
        booking.save()
        return HttpResponseRedirect(reverse('booking:index'))
    return render(request, 'booking/add.html')
