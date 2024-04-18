from apps.users.models import User, Query
from django.contrib.auth.forms import UserChangeForm
from django import forms


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('text',)

