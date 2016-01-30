from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    context = {'body_text': 'About Me', 'title': "Carolyn's Portfolio", 'reasons': ["Height", "Hair Color", "Eye Color", "Skin Tone", "First Name", "Last Name"]}

    return render(request, 'index.html', context)
