from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import MovieList
from .serializers import MovieSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def main(request):
    if request.method == 'GET':
        movieslist = MovieList.objects.all()
        serializer = MovieSerializer(movieslist, many=True)
        return Response(serializer.data)
