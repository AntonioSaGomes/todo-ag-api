from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all().order_by("order")
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
def todo(request, id):
    try:
        todo = Todo.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('serializer',serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)