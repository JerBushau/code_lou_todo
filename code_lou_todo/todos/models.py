from django.core.urlresolvers import reverse
from django.db import models


# simple data model for todo
class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    is_complete = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todos:todo_detail",
                       kwargs={ "pk": self.pk })

