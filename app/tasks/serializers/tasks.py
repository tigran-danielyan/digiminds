from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ("user", )


class TaskUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("name", "description")
