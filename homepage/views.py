from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _
from .models import Article

# Create your views here


def home_view(request):

    # fetch the first article we created in admin
    article = Article.objects.order_by('-created_at').first()

    context = {
        'greeting': _("Welcome to our Localization Project!"),
        'large_number': 12345.67,
        'current_date': timezone.now(),
        'redirect_to': request.path,
        'article': article,
    }
    return render(request, 'home.html', context)