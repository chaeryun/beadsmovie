from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Media
from .serializers import MediaSerializer, MediaListSerializer


@api_view(["GET"])
def media(request):
    media_list = get_list_or_404(Media)
    serializers = MediaListSerializer(media_list, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def media_detail(request, media_pk: int):
    media = get_object_or_404(Media, pk=media_pk)
    serializers = MediaSerializer(media)
    return Response(serializers.data)
