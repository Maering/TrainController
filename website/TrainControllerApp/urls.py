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
    path('train/edit/<train_id>', views.train_edit, name='trains.edit'),
    path('train/update/<train_id>', views.train_update, name='trains.update'),
    path('train/delete/<train_id>', views.train_delete, name='trains.delete'),
    path('train/gallery', views.train_gallery, name='trains.gallery'),
    path('train/show/<train_id>', views.train_show, name='trains.show'),

    # Commands
    path('command/gallery', views.command_gallery, name='commands.gallery'),
    path('command/show/<command_id>', views.command_show, name='commands.show'),

    # Control panel
    path('controls/panel', views.control_panel, name='controls.panel'),
    # TODO: direct control of the train
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
