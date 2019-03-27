from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


def index_copy(request):
    return render(request, 'index_copy.html', locals())
