from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from event_management.views import *
from . import views

router = DefaultRouter()

urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('search', views.search, name="search"),
    path('reports', views.reports, name="reports"),
    path('profile', views.profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('users/<int:user_id>/delete', views.delete_user, name="delete_user"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('events', views.event_list, name="event_list"), 
    path('events/create', views.event_create, name="event_create"),
    path('events/<int:event_id>', views.event_edit, name="event_edit"),
    path('events/<int:event_id>/like', views.like_event, name="like_event"),
    path('events/<int:event_id>/report', views.report_event, name="report_event"),
    path('events/<int:event_id>/delete', views.event_delete, name="event_delete"),
    # re_path(r'^api/events$', views.event_list, name='event_list'),
    # re_path(r'^api/events/(?P<pk>[0-9]+)$', views.event_detail, name='event_detail'),
    path('location/', LocationApi, name='location-list'),
    path('location/<int:id>/', LocationApi, name='location-detail'),
    path('eventType/', EventTypeApi, name='eventType-list'),
    path('eventType/<int:id>/', EventTypeApi, name='eventType-detail'),
    path('eventTag/', EventTagApi, name='eventTag-list'),
    path('eventTag/<int:id>/', EventTagApi, name='eventTag-detail'),
    path('event/', EventApi, name='event-list'),
    path('event/<int:id>/', EventApi, name='event-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
