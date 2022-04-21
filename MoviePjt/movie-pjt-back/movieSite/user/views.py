import requests
from django.shortcuts import redirect, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

OAUTH_KAKAO_HOST = 'https://kauth.kakao.com'
OAUTH_KAKAO_CLIENT_ID = '5835235e4bcc589a0bd165c4d85651a8'
OAUTH_KAKAO_REDIRECTION_URL = 'http://localhost:8000/user/oauth/kakao/callback'

@api_view(["POST"])
def redirect_kakao_permission_code(request):
    response = redirect(f'{OAUTH_KAKAO_HOST}/oauth/authorize?client_id={OAUTH_KAKAO_CLIENT_ID}&redirect_uri={OAUTH_KAKAO_REDIRECTION_URL}&response_type=code')
    return response

@api_view(["GET"])
def kakao_login(request):
    payload = request.query_params
    if  not payload['code']:
        return request.error_description
    
    code = payload['code']
    header = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    body = {
        'grant_type': 'authorization_code',
        'client_id': OAUTH_KAKAO_CLIENT_ID,
        'redirect_uri': OAUTH_KAKAO_REDIRECTION_URL,
        'code': code,
    }
    response = requests.post(f'{OAUTH_KAKAO_HOST}/oauth/token', headers=header, data=body)
    
    payload = eval(response.content.decode())
    # r = eval(response.text)
    # if response.status_code != 200:
    #     response()
    #     return (r['error_code'], r['error_description'])

    ACCESS_TOKEN = payload['access_token']
    REFRESH_TOKEN = payload['refresh_token']

    header = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.get('https://kapi.kakao.com/v2/user/me', headers=header)
    payload = response.json()
    
    # TODO: 응답 에러 처리
    id = payload['id']
    email = payload['kakao_account']['email']
    user, is_created = User.objects.get_or_create(id=id, email=email, token=ACCESS_TOKEN)
    serializer = UserSerializer(user)

    return Response(data=serializer.data)
    
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
