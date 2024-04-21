### _Welcome to my repository!_
## 🎸 Stack:
- Language: Python🐍 version 3.10✅.
- Development approach: Django🔨 version 5.0.4, djangorestframework🔥 3.15.1.
## ⚙ Installation and usage:
### Dev server
#### 1. Go to IDE and run in terminal:
    git clone https://github.com/Nerogen/DRFKA.git
#### 2. Then run in terminal next line:
    pip install -r requirements.txt
#### 3. Nice, run in terminal next commands:
    python manage.py makemigrations 
    python manage.py migrate 
#### 4. Then start localhost:
    python manage.py runserver
### Docker
#### 1. Go to IDE and run in terminal:
    git clone https://github.com/Nerogen/DRFKA.git
#### 2. You also need installed docker with compose plugin:
    guide https://docs.docker.com/engine/install/
#### 3. Then run in terminal:
    docker-compose up -d --build
### K8s
#### 1. Go to your host with kubectl and clone repo:
    git clone https://github.com/Nerogen/DRFKA.git
#### 2. then apply files for deployment and service for access your app on 30001 port
    kubectl apply -f deploy/deploy.yaml
    kubectl apply -f deploy/service.yaml

## 😎 About app
#### Link manager for users in format of open API.
![image](https://github.com/Nerogen/Mogy-Tolko-Full-Stack/assets/72101790/0a901777-98e8-4036-b2b8-122ea91bb7bb)

#### Documentation
![image](https://github.com/Nerogen/Mogy-Tolko-Full-Stack/assets/72101790/c236ce83-8dce-4e7d-8899-ae6098bb2627)