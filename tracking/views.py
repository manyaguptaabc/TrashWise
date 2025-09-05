from django.shortcuts import render
from .models import WasteEntry, Location, UserProfile
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def dashboard(request):
    waste_entries = WasteEntry.objects.all().order_by('-timestamp')
    locations = Location.objects.all()
    users = UserProfile.objects.all()

    # 💡 Summary stats
    total_waste = WasteEntry.objects.aggregate(Sum('quantity_kg'))['quantity_kg__sum'] or 0
    total_locations = locations.count()
    total_users = users.count()

    context = {
        'waste_entries': waste_entries,
        'locations': locations,
        'users': users,
        'total_waste': total_waste,
        'total_locations': total_locations,
        'total_users': total_users,
    }

    return render(request, 'tracking/dashboard.html', context)
