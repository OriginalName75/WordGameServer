"""WordGameServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from CryptoMess.views import send_key, test, generate_full
from GameManager.views import read_game, send_letter, send_letter_grid
from UserManagement.views import register, root, check_connection, add_friend, \
    get_new_friend_list, new_friend_answer


urlpatterns = [
    url(r'^check_user/', check_connection),
    url(r'^register/', register),
    url(r'^get_key/', send_key),
    url(r'^get_new_friend_list/', get_new_friend_list),
    url(r'^add_friend/', add_friend),
    url(r'^new_friend_answer/', new_friend_answer),
    url(r'^read_game/', read_game),
    url(r'^send_letter/', send_letter),
    url(r'^send_letter_grid/', send_letter_grid),
    url(r'^test/', test),
    url(r'^generate_full/', generate_full),
    url(r'^', root),
]
