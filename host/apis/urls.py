from django.urls import path
from .views import get, create, patch

urlpatterns = [
    path('create/', create.create_host_view.as_view()),
    path('get/<str:host_name>/', get.get_host_view.as_view()),
    path('active/<int:host_id>/', patch.host_active_view.as_view()),
    path('inactive/<int:host_id>/', patch.host_inactive_view.as_view())
]