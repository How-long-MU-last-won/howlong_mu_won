from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Trophy
from .serializers import TrophySerializer


@api_view(["GET"])
def getTrophies(request):
    trophies = Trophy.objects.all()
    serializer = TrophySerializer(trophies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getTrophy(request, pk):
    trophy = Trophy.objects.get(id=pk)
    serializer = TrophySerializer(trophy, many=False)
    return Response(serializer.data)
