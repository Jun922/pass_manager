from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import App
from .forms import AppForm


class AppListView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/list.html'
    model = App
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            app_list = App.objects.filter(name__icontains=query, user=self.request.user)
        else:
            app_list = App.objects.all(user=self.request.user)
        return app_list


class AppCreateView(LoginRequiredMixin, generic.CreateView):
    model = App
    form_class = AppForm
    template_name = "app/form.html"
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AppUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = App
    fields = "__all__"
    template_name = "app/form.html"
    success_url = reverse_lazy("list")

    def get_success_url(self, **kwargs):
        pk = self.kwargs["pk"]
        return reverse_lazy("detail", kwargs={"pk": pk})
    
    def test_func(self, **kwargs):
        pk = self.kwargs["pk"]
        post = App.objects.get(pk=pk)
        is_user = post.user = self.request.user
        return is_user


class AppDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = App
    success_url = reverse_lazy('list')

    def test_func(self, **kwargs):
        pk = self.kwargs["pk"]
        post = App.objects.get(pk=pk)
        is_user = post.user = self.request.user
        return is_user