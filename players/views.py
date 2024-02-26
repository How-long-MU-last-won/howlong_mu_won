from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player, Position
from .serializers import PlayerSerializer, PositionSerializer
from coaches.models import Coach
from coaches.serializers import CoachSerializer
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


# Create your views here.
@api_view(["GET"])
def getPlayers(request):
    cache_key = "howlong_mu_won_players_getPlayers"
    if cache.get(cache_key):
        # print("cached")
        return Response(cache.get(cache_key))
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    cache.set(cache_key, serializer.data, timeout=60 * 60 * 24 * 7)
    return Response(serializer.data)


@api_view(["GET"])
def getPlayer(request, pk):
    player = Player.objects.get(id=pk)
    serializer = PlayerSerializer(player, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getByPosition(request, position_id):
    players = Player.objects.filter(position=position_id)
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getByCoachBought(request, coach_id):
    player = Player.objects.filter(boughtBy=coach_id)
    serializer = PlayerSerializer(player, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getAllCoachesWorkWith(request, pk):
    coaches = Player.objects.get(id=pk).workWith.all()
    serializer = CoachSerializer(coaches, many=True)
    return Response(serializer.data)


@receiver(post_save, sender=Player)
@receiver(post_delete, sender=Player)
def invalidate_cache_on_player_change(sender, instance, **kwargs):
    #  Invalidate all cached items
    cache.delete_many(keys=cache.keys("howlong_mu_won_players_*"))
