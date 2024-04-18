from django.urls import path

from apps.finder import views

app_name = 'finder'

urlpatterns = [
    path('', views.JobPostsView.as_view(), name='jobs'),
]
