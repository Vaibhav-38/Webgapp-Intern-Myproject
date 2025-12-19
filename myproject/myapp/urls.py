from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('',views.index,name='index'),
path('form',views.form,name='form'),
path('about',views.about,name='about'),
path('signup',views.signup,name='signup'),
path('signin',views.signin,name='signin'),
path('contact',views.contact,name='contact'),
path('service',views.service,name='service'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);