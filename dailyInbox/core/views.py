from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """The entry point for the website."""
    context = {}
    return render(request, 'core/index.html', context)
