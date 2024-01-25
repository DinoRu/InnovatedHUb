from django.shortcuts import render
from .forms import ContactForm


def index(request):
    form = ContactForm()
    return render(request, 'core/index.html', {'form': form})
