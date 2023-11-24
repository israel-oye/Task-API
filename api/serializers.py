from rest_framework import serializers
from .models import Task


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        """Used while retrieving value for the field."""
        return self._choices[obj]

    def to_internal_value(self, data):
        """Used while storing value for the field."""
        for i in self._choices:
            if self._choices[i] == data:
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))


class TaskSerializer(serializers.ModelSerializer):
    status = ChoiceField(choices=Task.STATUS_CHOICES)

    class Meta:
        model = Task
        fields = ["id", "name", "description", "status", "due_date", "creator"]

