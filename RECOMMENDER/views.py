from django.shortcuts import render

def movie(request):
    if request.method == 'GET':
        context ={}

    return render(request, 'movie.html',context)