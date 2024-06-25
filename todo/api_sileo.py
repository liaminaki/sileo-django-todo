from sileo.resource import Resource
from sileo.registration import register

from .models import Todo
from .forms import TodoForm


class TodoResource(Resource):

    query_set = Todo.objects.filter(removed=False)
    fields = ('label', 'id', 'done', 'todo_uuid')
    allowed_methods = ('filter','get_pk', 'create', 'delete','update')
    form_class = TodoForm
    delete_filter_fields = ['pk']
    update_filter_fields = ('pk',)
    

register(namespace="todo", name="todo", resource=TodoResource)
