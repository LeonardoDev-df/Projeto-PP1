# Projeto-PP1

SISTEMAS DE RESERVAS PARA UM RESTAURANTE

#instala máquina virtual
python -m venv env

#entra na pasta env
cd env

#caso de erro abra powersheel como admin e usa este código
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned 

#ativa máquina virtual
.\env\Scripts\Activate\.bat

#entrar na pasta
cd reservas

#instalando django
 pip install django

#cria super usuário
python manage.py createsuperuser

#cria models
python manage.py makemigrations

#cria tabelas no banco de dados
python manage.py migrate

#iniciando projeto
python manage.py runserver
