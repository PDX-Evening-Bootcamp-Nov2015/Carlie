from django.shortcuts import render

# Create your views here.
def RandomQuote(request):
    return render(request, 'RandomQuote/random_quote.html')
