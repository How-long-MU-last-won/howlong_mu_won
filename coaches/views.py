from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Coach
from .serializers import CoachSerializer
from players.serializers import PlayerSerializer
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


# Create your views here.
@api_view(["GET"])
def getCoaches(request):
    cache_key = "howlong_mu_won_coaches_getCoaches"
    if cache.get(cache_key):
        # print("cached")
        return Response(cache.get(cache_key))
    coaches = Coach.objects.order_by("-leadFrom").all()
    serializer = CoachSerializer(coaches, many=True)
    cache.set(cache_key, serializer.data, timeout=60 * 60 * 24 * 7)
    return Response(serializer.data)


@api_view(["GET"])
def getCoach(request, pk):
    coach = Coach.objects.get(id=pk)
    serializer = CoachSerializer(coach, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getAllPlayersWorkWith(request, pk):
    players = Coach.objects.get(id=pk).workWith.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@receiver(post_save, sender=Coach)
@receiver(post_delete, sender=Coach)
def invalidate_cache_on_coach_change(sender, instance, **kwargs):
    #  Invalidate all cached items
    cache.delete_many(keys=cache.keys("howlong_mu_won_coaches_*"))
