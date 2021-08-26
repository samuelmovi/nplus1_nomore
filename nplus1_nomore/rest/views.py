from django.db.models.query import Prefetch, prefetch_related_objects
from rest_framework import viewsets

# Create your views here.
from . import models, serializers

# Create your views here.


# GRANDPARENT

class GrandParentList(viewsets.ModelViewSet):

    model = models.GrandParent
    serializer_class = serializers.GrandParentSerializer
    queryset = model.objects.all()


class GrandParentListBad(viewsets.ModelViewSet):

    model = models.GrandParent
    serializer_class = serializers.GrandParentSerializerGood
    queryset = model.objects.all()


class GrandParentListGood(viewsets.ModelViewSet):

    model = models.GrandParent
    serializer_class = serializers.GrandParentSerializerGood

    def get_queryset(self):
        # annotate with reverse relationship
        queryset = self.model.objects.prefetch_related('parents')
        return queryset


# PARENT

class ParentListWorst(viewsets.ModelViewSet):

    model = models.Parent
    serializer_class = serializers.ParentSerializerBad
    queryset = model.objects.all()


class ParentListBad(viewsets.ModelViewSet):

    model = models.Parent
    serializer_class = serializers.ParentSerializerBad
    queryset = model.objects.select_related('parent')


class ParentListGood(viewsets.ModelViewSet):

    model = models.Parent
    serializer_class = serializers.ParentSerializerGood

    def get_queryset(self):
        children = Prefetch('children', queryset=models.GrandParent.objects.all())
        prefetch_related_objects(children)
        queryset = models.Parent.objects.select_related('parent')
        return queryset


# CHILDREN

class ChildListBad(viewsets.ModelViewSet):

    model = models.Child
    serializer_class = serializers.ChildSerializerGood
    queryset = model.objects.all()


class ChildListGood(viewsets.ModelViewSet):

    model = models.Child
    serializer_class = serializers.ChildSerializerGood
    queryset = model.objects.select_related('parent')
