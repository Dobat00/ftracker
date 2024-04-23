from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from main.forms import LoginForm, CadastroForm, GastoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from main.models import Gasto
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        gastos = list(Gasto.objects.values())
        print(gastos)
        return Response(gastos)


def deleteall(request):
    a = Gasto.objects.all().delete()
    return redirect('dashboard')


def teste(request):
    a = Gasto.objects.get(pk=1)
    print(request.user.id)
    return HttpResponse('funciona')


def login(request):
    form = LoginForm()
    if(request.method == "POST"):
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context)


def cadastro(request):
    form = CadastroForm()
    if (request.method == 'POST'):
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'main/cadastro.html', context)


@login_required(login_url='login')
def dashboard(request):
    # gastos_list = Gasto.objects.all()
    gastos_list = Gasto.objects.filter(user=request.user)
    valortotal = 0
    categoria_lista = []
    for gasto in gastos_list:
        valortotal = gasto.valor + valortotal
    for i in Gasto.categoria_lista:
        categoria_lista.append(i[0])
    print(categoria_lista)
    context = {
        'gastos': gastos_list,
        'valortotal': valortotal,
        'categoria_lista': categoria_lista,
        'current_user': request.user,
    }
    return render(request, 'main/dashboard.html', context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def gasto(request):
    if (request.method == 'POST'):
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.user = request.user
            # print('REQUEST.USER: ', request.user)
            # print('FORM.USER_ID:', form.user_id)
            # print('REQUEST.USER.ID:', request.user.id)
            gasto.save()

            return redirect('dashboard')
    else:
        form = GastoForm()
        context = {
            'form': form
        }
        return render(request, 'main/gasto.html', context)


@login_required(login_url='login')
def deletar(request, gasto_id):
    gasto = Gasto.objects.get(pk=gasto_id)
    context = {
        "gasto": gasto
    }
    return render(request, 'main/deletar.html', context)


@login_required(login_url='login')
def deletar_post(request, gasto_id):
    Gasto.objects.get(id=gasto_id).delete()
    return redirect('dashboard')


@login_required(login_url='login')
def editar(request, gasto_id):
    gasto = get_object_or_404(Gasto, pk=gasto_id, user=request.user)
    form = GastoForm(instance=gasto)
    context = {
        'gasto': gasto,
        'form': form,
    }
    if (request.method == 'POST'):
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'main/editar.html', context)


# @login_required(login_url='login')
# def editar_post(request, gasto_id):
#     gasto = get_object_or_404(Gasto, pk=gasto_id)
#     if (request.method == 'POST'):
#         novo_gasto =
#     return redirect('dashboard')
