from django.shortcuts import render


def IndexView(request):
    template='index.html'
    return render(request, template)