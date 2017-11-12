from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

# the generic views hook up to the appropriate template automagically,
# based on the name of the template. It can also be specified as it is
# in the update view.

# generic list view
class TodoList(generic.ListView):
    model = models.Todo

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('is_complete', '-created_at')

    def get_context_data(self, *args, **kwargs):
        context = super(TodoList, self).get_context_data(*args, **kwargs)
        todos = models.Todo.objects.all()
        context['active_todos'] = todos.filter(is_complete=False).order_by('-created_at')
        context['complete_todos'] = todos.filter(is_complete=True).order_by('-created_at')
        return context

# genetic detail view
class TodoDetail(generic.DetailView):
    model = models.Todo

    # in addition to the individual todo also grab the others for the nav
    # get just entries create just before and just after
    def get_context_data(self, *args, **kwargs):
        context = super(TodoDetail, self).get_context_data(*args, **kwargs)
        # figure out how to use annotate!!!! seems like it would help here
        if context['todo'].is_complete == True:
            all_todos = models.Todo.objects.all().filter(is_complete=True)
        else:
            all_todos = models.Todo.objects.all().filter(is_complete=False)
        context['todo'].content = context['todo'].content.strip()
        context['before'] = all_todos.filter(
            created_at__gt=context['todo'].created_at).order_by(
                'created_at')[:1]
        context['after'] = all_todos.filter(
            created_at__lt=context['todo'].created_at).order_by(
                '-created_at')[:1]
        #find out if todo has been edited
        if context['todo'].created_at.replace(microsecond=0) != context['todo'].modified_at.replace(microsecond=0):
            context['modded'] = True
        return context


# generic create view
class TodoCreate(generic.CreateView):
    model = models.Todo
    form_class = forms.TodoForm


# generic update view
class TodoUpdate(generic.UpdateView):
    model = models.Todo
    fields = ['title', 'content', 'is_complete']
    template_name_suffix = '_update_form'


# generic delete view
class TodoDelete(generic.DeleteView):
    model = models.Todo
    success_url = reverse_lazy('todos:todo_list')
