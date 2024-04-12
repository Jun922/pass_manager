"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path

os.path.join(os.path.dirname(__file__), '../')
from pw_recorder.views import AppListView, AppCreateView, AppUpdateView, AppDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AppListView.as_view(), name='list'),
    path('create/', AppCreateView.as_view(), name='create'),
    path('<int:pk>/update/', AppUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', AppDeleteView.as_view(), name='delete'),
]