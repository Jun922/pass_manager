from django.urls import reverse_lazy
from django.views import generic
from .models import App
from .forms import AppForm


class AppListView(generic.ListView):
    template_name = 'app/list.html'
    model = App
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            app_list = App.objects.filter(name_icontains=query)
        else:
            app_list = App.objects.all()
        return app_list



class AppCreateView(generic.CreateView):
    model = App
    form_class = AppForm
    template_name = "app/form.html"
    success_url = reverse_lazy("list")


class AppUpdateView(generic.UpdateView):
    model = App
    fields = "__all__"
    template_name = "app/form.html"
    success_url = reverse_lazy("list")


class AppDeleteView(generic.DeleteView):
    model = App
    template_name = "app/confirm_delete.html"
    success_url = reverse_lazy('list')