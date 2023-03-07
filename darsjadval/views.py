from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Darsjadval

class DarsjadvalListView(ListView):
    model = Darsjadval
    template_name = 'jadval_list.html'

class DarsjadvalDetailView(DetailView):
    model = Darsjadval
    template_name = 'jadval_detail.html'

class DarsjadvalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Darsjadval
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'jadval_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DarsjadvalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Darsjadval
    template_name = 'jadval_delete.html'
    success_url = reverse_lazy('jadval_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DarsjadvalCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Darsjadval
    template_name = 'jadval_new.html'
    fields = ('title', 'summary', 'body', 'photo',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

