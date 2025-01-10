from django.shortcuts import render
from .forms import MessageForm
# Create your views here.


def test(request):
    return render(request, 'form.html', context={'form': MessageForm()})
