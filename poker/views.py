from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'gameroom.html', {
        'room':room_name
    })