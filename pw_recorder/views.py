from django.views import generic
from .models import App


class AppListView(generic.ListView):
    template_name = 'app/list.html'
    model = App

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            app_list = App.objects.filter(name__icontains=query)
        else:
            app_list = App.objects.all()
        return app_list