from rest_framework import serializers

from . import models

# GRANDPARENTS

class GrandParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GrandParent
        fields = '__all__'


class GrandParentSerializerGood(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')

    def get_children(self, grandparent):
        # Use reverse relation instead of querying the Model
        # queryset = models.Parent.objects.filter(parent=grandparent)
        queryset = grandparent.parents.all()
        serialized_data = GrandParentSerializer(queryset, many=True, read_only=True, context=self.context)
        return serialized_data.data

    class Meta:
        model = models.GrandParent
        fields = '__all__'


# PARENTS

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Parent
        fields = '__all__'


class ParentSerializerBad(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')

    def get_children(self, parent):
        queryset = models.Child.objects.filter(parent=parent)
        serialized_data = ChildSerializerGood(queryset, many=True, read_only=True, context=self.context)
        return serialized_data.data

    class Meta:
        model = models.Parent
        fields = '__all__'


class ParentSerializerGood(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')

    def get_children(self, parent):
        queryset = models.Child.objects.filter(parent=parent).select_related('parent')
        serialized_data = ChildSerializerGood(queryset, many=True, read_only=True, context=self.context)
        return serialized_data.data

    class Meta:
        model = models.Parent
        fields = '__all__'

# CHILDREN

class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Child
        fields = '__all__'


class ChildSerializerGood(serializers.ModelSerializer):
    parent = ParentSerializer()

    class Meta:
        model = models.Child
        fields = '__all__'

