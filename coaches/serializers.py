from rest_framework import serializers
from .models import Coach


class CoachSerializer(serializers.ModelSerializer):
    trophyWon = serializers.SlugRelatedField(
        read_only=True, slug_field="name", many=True
    )

    class Meta:
        model = Coach
        fields = "__all__"
