from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from django.contrib.auth.models import User, auth
from .forms import RoomForm
from django.contrib import messages

'''
Room = [
    {'id': 1, 'name': 'Ovie', 'description': 'He has a big head'},
    {'id': 2, 'name': 'Emma', 'description': 'He has a big leg'},
    {'id': 3, 'name': 'Tega', 'description': 'He has a big mouth'},
        ]


def profiles(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}

    return render(request, 'profile_page.html', context)
'''

def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect('/')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'username already exist')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('signin')
        else:
            messages.error(request, 'password mismatch')
            return redirect('/')

    return render(request, 'index.html', context)

def signin_form (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'login in successful')
            return redirect ('/')
        else:
            messages.error(request, 'wrong credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def signout(request):
    auth.logout(request)
    return redirect('/')

def profile_page(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'profile.html', context)

def createform(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'form.html', context)

def update_form(request, pk):
    room = Room.objects.get(id=pk)  #This would give bring out the particular room, 
    form = RoomForm(instance=room)  #This would give you the form of the particular room selected by id
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'form.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('/')


    return render(request, 'delete.html', {'obj': room})