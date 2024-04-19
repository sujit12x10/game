from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('matches/', views.match, name='matches'),
    path('season/<int:num>/-matches/', views.get_season, name='get_matches'),
    path('play/<int:id>/', views.play, name='play'),
    path('season/<int:num>/points-table/', views.points_table, name='points_table'),
    path('season/<int:num>/playoffs/', views.playoffs, name='playoffs'),
    path('season/<int:num>/playoffs-play/', views.playoffs_play, name='playoffs_play'),
]