from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.addshow),
    path('shows/create', views.create),
    path('shows/<num>', views.tvshow),
    path('shows/<num>/edit', views.editshow),
    path('shows/<num>/delete', views.delete),
    path('second/<name>', views.second),
]
