from django.shortcuts import render
from django.utils import timezone
# Create your views here


def home_view(request):
    context = {
        'greeting': "Welcome to our Localization Project!",
        'large_number': 12345.67,
        'current_date': timezone.now()
    }
    return render(request, 'home.html', context)