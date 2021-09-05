from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path('main',views.main, name="main"),
    path('',views.index, name="index"),
    path('add',views.add, name="add"),
    path('update/<int:id>/', views.EditView.as_view(), name='update'),
    path('delete/<int:id>/', views.DeleteView.as_view(), name='delete'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
]