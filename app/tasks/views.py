from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from tasks.models import Task
from tasks.serializers.tasks import TaskSerializer, TaskCreateSerializer, TaskUpdateSerializer


class TaskViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tasks = Task.objects.filter(user=request.user).order_by('name')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"errors": f"{serializer.errors}"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskActionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({"message": "there is no task with this id found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, task_id):
        task = Task.objects.filter(id=task_id, user=request.user).first()

        if not task:
            return Response({"message": "there is no task with this id found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskUpdateSerializer(task, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response({"errors": f"{serializer.errors}"}, status.HTTP_422_UNPROCESSABLE_ENTITY)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, task_id):

        try:
            Task.objects.get(id=task_id, user=request.user).delete()
        except Task.DoesNotExist:
            return Response({"message": "there is no task with this id found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


