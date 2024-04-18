from django.urls import path

from .views import QueryCreateView

app_name = 'users'

urlpatterns = [
    path("profile/edit", QueryCreateView.as_view(), name="edit_profile"),
]
