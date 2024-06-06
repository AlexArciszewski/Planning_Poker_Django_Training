from django.shortcuts import render


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()         #zapisz formualrz
    else:
        form = UserCreationForm()#pusty formularz

    return render(request, 'users/register.html', {"form": form})


def homepage(request):
    """strona startowa"""

    return render(request, 'users/index.html')
