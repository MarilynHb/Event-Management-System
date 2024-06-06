from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from event_management.views import *
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'eventtypes', EventTypeViewSet, basename='eventtypes')
router.register(r'eventtags', EventTagViewSet, basename='eventtags')
router.register(r'events', EventViewSet, basename='events')
router.register(r'likedevents', LikedEventsViewSet, basename='likedevents')
router.register(r'reportevents', ReportEventViewSet, basename='reportevents')
router.register(r'filelinks', FileLinkViewSet, basename='filelinks')

urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('search', views.search, name="search"),
    path('reports', views.reports, name="reports"),
    path('profile', views.profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('events', views.event_list, name="event_list"), 
    path('events/create', views.event_create, name="event_create"),
    path('events/<int:event_id>', views.event_edit, name="event_edit"),
    path('events/<int:event_id>/like', views.like_event, name="like_event"),
    path('events/<int:event_id>/report', views.report_event, name="report_event"),
    path('events/<int:event_id>/delete', views.event_delete, name="event_delete"),
    path('api/', include(router.urls)),  # Include the router URLs here
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
