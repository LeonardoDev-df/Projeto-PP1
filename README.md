# Projeto-PP1

SISTEMAS DE RESERVAS PARA UM RESTAURANTE


https://github.com/LeonardoDev-df/Projeto-PP1/assets/69646199/6ad1af81-5f7d-40af-8ce2-14ce7166420c



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
