from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'JavaPic/gallery.html')

def join(request):
    return render(request, 'JavaPic/join.html')

def index(request):
    return render(request, 'JavaPic/index.html')
