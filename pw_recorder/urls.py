from django.urls import path
from .views import AppListView, AppCreateView, AppUpdateView, AppDeleteView


app_name = "pw_recorder"
urlpatterns = [
    path('list/', AppListView.as_view(), name='list'),
    path('create/', AppCreateView.as_view(), name='create'),
    path('<int:pk>/update/', AppUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', AppDeleteView.as_view(), name='delete'),
]