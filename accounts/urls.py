from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^profile/(?P<user_id>\d+)/$', views.profile_view, name='profile'),
]
