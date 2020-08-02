from django.shortcuts import render

# Create your views here.
from .models import FilmReview

def movies_short(request):
    ###  从models取数据传给template  ###
    shorts = FilmReview.objects.all()

    return render(request, 'result.html', locals())
