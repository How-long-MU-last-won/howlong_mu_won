from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Trophy
from .serializers import TrophySerializer
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


@api_view(["GET"])
def getTrophies(request):
    cache_key = "howlong_mu_won_trophies_getTrophies"
    if cache.get(cache_key):
        # print("cached")
        return Response(cache.get(cache_key))
    trophies = Trophy.objects.all()
    serializer = TrophySerializer(trophies, many=True)
    cache.set(cache_key, serializer.data, timeout=60 * 60 * 24 * 7)
    return Response(serializer.data)


@api_view(["GET"])
def getTrophy(request, pk):
    trophy = Trophy.objects.get(id=pk)
    serializer = TrophySerializer(trophy, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getTrophyByCoach(request, coach_id):
    trophy = Trophy.objects.filter(lastWonBy=coach_id)
    serializer = TrophySerializer(trophy, many=True)
    return Response(serializer.data)


@receiver(post_save, sender=Trophy)
@receiver(post_delete, sender=Trophy)
def invalidate_cache_on_trophy_change(sender, instance, **kwargs):
    #  Invalidate all cached items
    cache.delete_many(keys=cache.keys("howlong_mu_won_trophies_*"))
