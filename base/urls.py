from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name="home"),
    path('room/<str:primaryKey>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:primaryKey>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:primaryKey>/', views.deleteRoom, name="delete-room")
]
