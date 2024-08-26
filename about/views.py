from django.shortcuts import render

from .forms import CollaborateForm
from .models import About


# Create your views here.
def about_me(request):
    """
    Render the About page
    """
    about = About.objects.all().order_by("-updated_on").first
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
        "about": about,
        "collaborate_form": collaborate_form
        },
    )
