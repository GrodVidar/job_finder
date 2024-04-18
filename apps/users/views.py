from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from apps.users.models import Query
from apps.users.forms import QueryForm


class QueryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Query
    form_class = QueryForm
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('users:edit_profile')

    def form_valid(self, form):
        query = form.save(commit=False)
        query.save()

        self.request.user.queries.add(query)
        return super().form_valid(form)
