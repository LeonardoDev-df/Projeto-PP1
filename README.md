# Projeto-PP1

SISTEMAS DE RESERVAS PARA UM RESTAURANTE




https://github.com/LeonardoDev-df/Projeto-PP1/assets/69646199/855a05ee-86f6-4394-a744-1fb3d562c49c


#entrar na pasta
-------------------------------------------------------------
cd reservas

#instala máquina virtual
-------------------------------------------------------------
python -m venv env

#caso de erro abra powersheel como admin e usa este código
--------------------------------------------------------------
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned 

#ativa máquina virtual
-------------------------------------------------------------
.\env\Scripts\Activate\.bat

#instalando django
-------------------------------------------------------------
 pip install django

#cria super usuário
-------------------------------------------------------------
python manage.py createsuperuser

#cria models
-------------------------------------------------------------
python manage.py makemigrations

#cria tabelas no banco de dados
-------------------------------------------------------------
python manage.py migrate

#iniciando projeto
-------------------------------------------------------------
python manage.py runserver
