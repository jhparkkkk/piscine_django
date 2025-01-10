import os
from django.shortcuts import render
from .forms import MessageForm

from pathlib import Path
import logging
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent


def test(request):

    if request.method == 'POST':
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['message'])
        return HttpResponseRedirect("/ex02")

    history = []
    with open(os.path.join(BASE_DIR, 'logs'), 'r') as f:
        for line in f:
            history.append(line)
    return render(request, 'form.html', context={'form': MessageForm(),
                                                 'history': history})
