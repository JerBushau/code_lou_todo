from django import forms

from . import models


# specifies how the form will be presented in the update and create templates
class TodoForm(forms.ModelForm):
    class Meta:
        fields = ("title", "content")
        model = models.Todo
