from django.shortcuts import render

# Create your views here.
def AngryDice(request):

    return render(request, 'AngryDice/Angry_Dice.html')
