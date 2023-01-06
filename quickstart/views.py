from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer


def todo_list(request):

    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return JsonResponse(serializer.data, safe=False)

def add_todo(request):

    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return JsonResponse(serializer.data, safe=False)

# Create your views here.
