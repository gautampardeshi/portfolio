from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('project1/',views.project1, name='project1'),
    path('project/',views.project, name='project'),
    # path('register/',views.register,name='register'),
    # path('login/', views.login, name='login'),

]
