# Freq4py
Projeto feito em Python que cria de forma automatizada a folha de frequência. 

## Subir projeto

### Subir containers
    docker-compose up

### Migrar com o banco
    docker-compose run --rm app python manage.py migrate

### Criar super usuario (Optional)
    docker-compose run --rm app python manage.py createsuperuser

## Aplicação

### Admin Dashboard (WEB)
    localhost:8000/admin
### Chamadas REST
#### Login
    http://localhost:8000/api/login/
#### Register
    http://localhost:8000/api/register/
#### sheets
    http://localhost:8000/api/sheets/
#### schedules
    http://localhost:8000/api/schedules/
#### notworkingdays
    http://localhost:8000/api/notworkingdays/
#### notworkingtypes
    http://localhost:8000/api/notworkingtypes/
#### titles
    http://localhost:8000/api/titles/
#### values
    http://localhost:8000/api/values/
#### exportdocx
    http://localhost:8000/api/exportdocx/
