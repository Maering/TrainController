from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),

    # Dashboard
    path('dashboard', views.dashboard, name='dashboard'),

    # Trains
    path('train/new', views.train_new, name='trains.new'),
    path('train/register', views.train_register, name='trains.register'),
    path('train/<train_id>/edit', views.train_edit, name='trains.edit'),
    path('train/<train_id>/update', views.train_update, name='trains.update'),
    path('train/<train_id>/delete', views.train_delete, name='trains.delete'),
    path('train/<train_id>/show', views.train_show, name='trains.show'),
    path('train/gallery', views.train_gallery, name='trains.gallery'),

    # Commands
    path('command/gallery', views.command_gallery, name='commands.gallery'),
    path('command/show/<command_id>', views.command_show, name='commands.show'),

    # Control panel
    path('controls/panel', views.control_panel, name='controls.panel'),
    path('controls/process', views.control_process, name='controls.process')
    # TODO: direct control of the train
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
