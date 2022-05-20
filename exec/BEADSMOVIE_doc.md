# BEADSMOVIE

### Server

- nginx 설치

  ```shell
  # apt repository 에 설치하고자 하는 nginx 버전 추가 
  # ubuntu 버전 (18.04: bionic, 16.04: xenial)
  $ sudo touch /etc/apt/sources.list.d/nginx.list
 
  # 저장소 업데이트
  $ sudo apt-get update
  
  # nginx 설치
  $ sudo apt-get install nginx
  ```

- mongDB 설치

  ```shell
  # 우분투 서버 업데이트
  $ sudo apt-get update
  
  # mongodb-server 설치
  sudo apt-get install -y mongodb-org
  
  # 방화벽 설정
  $ sudo ufw allow mongod
  
  # mongoDB 실행
  $ sudo service mongod start
  ```

  

- python 및 기타 라이브러리 설치

  ```shell
  # apt 업데이트
  $ sudo apt-get update && sudo apt-get upgrade
  
  # requriement.txt 설치
  $ pip3 install -r requirements.txt
  
  # 설치 확인
  $ python3 -V
  ```
  
  
  
- git 설치

  ```shell
  # 패키지 리스트 업데이트
  $ sudo apt-get install git
  
  # 깃 설치
  $ sudo apt install git
  
  # 설치 후 버전 확인
  $ git --version
  ```

  

- node js 및 npm 설치

  ```shell

  # apt 업데이트
  $ sudo apt-get update && sudo apt-get upgrade

  # node js 설치
  $ sudo apt install nodejs
  
  # npm 설치
  $ sudo apt-get install npm
  
  ```

- 방화벽

  1) 설치
     ```shell
     $ apt-get install ufw
     ```

  2) 설정

     ```shell
     $ ufw allow ssh
     $ ufw allow 80/tcp
     $ ufw enable
     ```



### MongoDB Compass 접속

```MongoDB
15.165.17.189:27017
```



### Build & Deploy

- Backend 빌드 및 배포

  - 먼저 git에서 받아 온 후

  - ```shell
    $python3 -m venv myvenv
    
    $source myvenv/bin/activate
    
    $pip3 install -r requirements.txt
    ```
    
  - 서버에서 실행

    ```shell
    python3 manage.py runserver 0:8000
    
    pyth manage.py makemigrations
    
    python manage.py migrate
    ```



- uwsgi 설정

```uwsgi
[uwsgi]

chdir = /home/ubuntu/S06P31C201/MoviePjt/movie-pjt-back
module = BEADSMOVIE.wsgi:application
home = /home/ubuntu/myvenv/

uid = ubuntu
gid = ubuntu

socket = /tmp/BEADSMOVIE.sock
chmod-socket = 666
chown-socket = ubuntu:ubuntu

enable-threads = true
master = true
vacuum = true
pidfile = /tmp/BEADSMOVIE.pid
logto = /var/log/uwsgi/BEADSMOVIE/@(exec://date +%%Y-%%m-%%d).log
log-reopen = true
```



- Nginx 설정

```nginx
server {

    listen 80;
    server_name beadsmovie.com;
    charset utf-8;
    client_max_body_size 128M;


    location / {
        alias /var/www/html/dist/;
        try_files $uri $uri/ index.html;
    }


    location /api/ {
        uwsgi_pass  unix:///tmp/BEADSMOVIE.sock;
        include     uwsgi_params;
    }

    location /static/ {
        alias /home/ubuntu/S06P31C201/MoviePjt/movie-pjt-back/static/;
    }

    if ($http_x_forwarded_proto = 'http'){
        return 301 https://$host$request_uri;
    }

    if ($host = 'beadsmovie.com') {
        return 301 https://www.beadsmovie.com$request_uri;
    }

}

```





- Frontend 빌드 및 배포

  - movie-pjt-front 로 이동

    ```shell
    $ npm install
    $ npm run build
    ```

- dist 파일을 생성 후 /var/www/html에 위치

  ```shell
  sudo cp -f /home/ubuntu/S06P31C201/MoviePjt/movie-pjt-back/.config/nginx/BEADSMOVIE.conf /etc/nginx/sites-available/BEADSMOVIE.conf
  
  
  sudo ln -sf /etc/nginx/sites-available/BEADSMOVIE.conf /etc/nginx/sites-enabled/BEADSMOVIE.conf
  
  
  sudo systemctl daemon-reload
  sudo systemctl restart uwsgi nginx
  ```



---

Notion 참고 : https://berry-giant-e1b.notion.site/7d919546328a4a018c3ab6a260a69da6
