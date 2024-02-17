from rest_framework import serializers
from .models import Player, Position


class PlayerSerializer(serializers.ModelSerializer):
    boughtBy = serializers.SlugRelatedField(
        read_only=True, slug_field="name"  # Specify the field to display
    )
    workWith = serializers.SlugRelatedField(
        read_only=True, slug_field="name", many=True  # Specify the field to display
    )
    position = serializers.SlugRelatedField(
        read_only=True, slug_field="position"  # Specify the field to display
    )

    class Meta:
        model = Player
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"
