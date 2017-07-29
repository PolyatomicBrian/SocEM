from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^identities', views.identities, name='identities'),
    url(r'^profiles', views.profiles, name='profiles'),
    url(r'^emails', views.emails, name='emails'),
    url(r'^hosting', views.hosting, name='hosting'),
    url(r'^', views.index, name='index'),
]
