from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Coach
from .serializers import CoachSerializer
from players.serializers import PlayerSerializer


# Create your views here.
@api_view(["GET"])
def getCoaches(request):
    coaches = Coach.objects.all()
    serializer = CoachSerializer(coaches, many=True)
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
