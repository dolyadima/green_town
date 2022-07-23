from rest_framework import generics
from apps.trees.models import Tree
from apps.trees.serializers import TreeSerializer


class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer


class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
