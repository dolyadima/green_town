from rest_framework import generics
from apps.trees.models import Tree
from apps.trees.serializers import TreesSerializer, TreeDetailSerializer


class TreesList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreesSerializer


class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeDetailSerializer
