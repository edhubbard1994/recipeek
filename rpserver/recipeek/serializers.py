from rest_framework import serializers
from .models import RecipeModel

class RecipeSerializer(serializers.Serializer):
    class Meta:
        model = RecipeModel

        fields = ('id','name','meal','ingredients','instructions','tags',)