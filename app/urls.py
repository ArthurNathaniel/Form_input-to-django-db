from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('create_user', views.create_user, name='create_user'),
    path('success_page', views.success_page, name='success_page'),
    path('user_list', views.user_list, name='user_list'),

]
