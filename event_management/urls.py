from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('search', views.search, name="search"),
    path('profile', views.profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('user_logout', views.user_logout, name="user_logout"),

    path('events', views.event_list, name="event_list"), 
    path('events/create', views.event_create, name="event_create"),
    path('events/<int:event_id>', views.event_edit, name="event_edit"),
    path('events/<int:event_id>/delete', views.event_delete, name="event_delete"),


]