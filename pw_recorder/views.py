from django.views import generic
from .models import App
from .forms import AppForm


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



class AppCreateView(generic.CreateView):
    model = App
    form_class = AppForm
    template_name = "app/form.html"
    success_url = "/"