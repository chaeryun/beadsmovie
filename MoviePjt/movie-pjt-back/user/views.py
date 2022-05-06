import json
import requests
from django.shortcuts import redirect, get_list_or_404
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from bson import json_util
from .models import User
from .serializers import UserSerializer

@api_view(["POST"])
@permission_classes((AllowAny,))
def kakao_login(request):
    kakao_access_token = request.headers['Kakao']
    if  not kakao_access_token:
        return request.error_description
    
    header = {'Authorization': f'Bearer {kakao_access_token}'}
    response = requests.get('https://kapi.kakao.com/v2/user/me', headers=header)
    payload = response.json()
    
    # TODO: 응답 에러 처리
    id = payload['id']
    email = payload['kakao_account']['email']
    nickname = payload['properties']['nickname']
    user, is_created = User.objects.get_or_create(kakao_id=id, email=email, username=nickname)
    serializer = UserSerializer(user)

    refresh = RefreshToken.for_user(user)
    return Response(data={
        'user' : serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
    
@api_view(["GET"])
def kakao_logout(request):
    # ACCESS_TOKEN = request.header['token']
    # 프론트와 토큰 API 협의되면 수정
    ACCESS_TOKEN = 'jZcplssfEw3flVXVEXxB9kJUD_GPWZnj2zOYuAo9cxgAAAGAScum7w'
    header = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.post('https://kapi.kakao.com/v1/user/logout', headers=header)
    # TODO: 사용자 권한 인증시 나오는 kakao id와 응답값으로 오는 kakao id를 비교해 검증하고 user의 token값을 무효화할 것
    payload = response.json()

    return Response(payload)
