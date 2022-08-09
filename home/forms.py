from django import forms
from .models import ToDo


class NewTodoForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput, max_length=30)
    body = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField()


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'body', 'created')
