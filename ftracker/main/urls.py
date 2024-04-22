from django.contrib import admin
from django.urls import path
from main import views
from main.views import ChartData

urlpatterns = [
    path('teste', views.teste, name='teste'),
    path('api/chartdata', ChartData.as_view(), name='chartdata'),
    path('', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('gasto', views.gasto, name='gasto'),
    path('deletar/<int:gasto_id>', views.deletar, name='deletar'),
    path('deletar_post/<int:gasto_id>', views.deletar_post, name='deletar_post'),
    path('editar/<int:gasto_id>', views.editar, name='editar'),
]
