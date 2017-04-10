from django.conf.urls import url
from .views import HomeView, ProfileView, PeopleView

urlpatterns = [
    url(r'^home', HomeView.as_view(), name='home'),
    url(r'^profile',ProfileView.as_view(), name='profile'),
    url(r'^people',PeopleView.as_view(), name='people')
]