from rest_framework import serializers
from apps.trees.models import Tree


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = [
            'pk',
            'registration_number',
            'x_coord',
            'y_coord',
            'crown_radius',
            'age',
            'type',
            'condition',
            'photo_path',
            'list_tasks',
        ]
