from django.contrib import admin
from apps.trees.models import Tree


class TreeAdmin(admin.ModelAdmin):
    model = Tree
    list_display = ['registration_number', 'type', 'age', ]

    # def get_name(self, obj):
    #     return obj.author.name
    # get_name.admin_order_field = 'author'  #Allows column order sorting
    # get_name.short_description = 'Author Name'  #Renames column head

    # Filtering on side - for some reason, this works
    list_filter = ['type', 'age', ]


admin.site.register(Tree, TreeAdmin)
