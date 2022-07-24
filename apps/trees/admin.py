from django.contrib import admin
from apps.trees.models import Tree


class TreeAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'type', 'age')


admin.site.register(Tree)
