from django.views import generic
from .models import App


class AppListView(generic.ListView):
    template_name = 'app/list.html'
    model = App