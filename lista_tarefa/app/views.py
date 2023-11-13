from django.shortcuts import render

def todos(request):
    return render(request, 'todo/index.html')


