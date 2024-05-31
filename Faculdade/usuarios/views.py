from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('ja cadastrado')

        # criaçao de usuario
        user = User.objects.create_user(
            username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuario cadastrado com sucesso')

        return HttpResponse(username)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)

            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Usuario ou senha invalidos')


def plataforma(request):
    return HttpResponse('plataforma')
