from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    This serializer is responsible for converting Task instances to JSON format 
    and validating incoming data for Task creation and updates.

    Meta:
        model (Task): The Task model to serialize.
        fields (list): List of fields to include in the serialization.
    """
    class Meta:
        model = Task
        fields = [
            "id", "title", "description",
            "due_date", "assigned_to",
            "status", "created_at",
        ]
