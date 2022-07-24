from rest_framework import serializers
from apps.trees.models import Tree


class TreesSerializer(serializers.ModelSerializer):
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

    type = serializers.SerializerMethodField()
    condition = serializers.SerializerMethodField()

    def get_type(self, tree_obj):
        tree = Tree.objects.get(pk=tree_obj.pk)
        return tree.get_type_display()

    def get_condition(self, condition_obj):
        tree = Tree.objects.get(pk=condition_obj.pk)
        return tree.get_condition_display()


class TreeDetailSerializer(serializers.ModelSerializer):
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

    type = serializers.SerializerMethodField()
    condition = serializers.SerializerMethodField()
    list_tasks = serializers.SerializerMethodField()

    def get_type(self, tree_obj):
        tree = Tree.objects.get(pk=tree_obj.pk)
        return tree.get_type_display()

    def get_condition(self, condition_obj):
        tree = Tree.objects.get(pk=condition_obj.pk)
        return tree.get_condition_display()

    def get_list_tasks(self, list_tasks_obj):
        if len(list_tasks_obj.list_tasks) == 1:
            return list_tasks_obj.list_tasks[0]
        elif len(list_tasks_obj.list_tasks) > 1:
            return ','.join(list_tasks_obj.list_tasks)
        return '-'
