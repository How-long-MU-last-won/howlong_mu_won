from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player, Position
from .serializers import PlayerSerializer, PositionSerializer
from coaches.models import Coach
from coaches.serializers import CoachSerializer


# Create your views here.
@api_view(["GET"])
def getPlayers(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
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
