from django.urls import path
from shop import views
from django.conf import settings
from django.contrib.auth import logout

urlpatterns = [
    path('', views.search_dishes, name="index"),
    path('category/', views.view_category, name="category"),
    # user actions
    path('edit/', views.edit_profile, name="edit"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name='log_out'),
    path('register/', views.register, name="register"),

]