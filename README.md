# Projeto-PP1

SISTEMAS DE RESERVAS PARA UM RESTAURANTE

#layout figma link 
https://www.figma.com/file/MdTXQhYzpyj1dTWmPQRtRe/Telas-Programa%C3%A7%C3%A3o-para-Internet-1?type=design&node-id=0-1
_____________________________________________________________________________
#modelo banco de daos

_____________________________________________________________________________

#regras de negócio
* limte de mesas disponíveis 20
* aviso quando estiver lotado ou sem mesas disponíveis
* horários de reservas proibido entre 00:00 e 10:00 manhã
_____________________________________________________________________________
#vídeo apresentação
https://github.com/LeonardoDev-df/Projeto-PP1/assets/69646199/8f5a5ad2-4692-4750-bbb7-d40ca9e11d98

#entrar na pasta
cd reservas
_____________________________________________________________________________

python -m venv env
_____________________________________________________________________________

#caso de erro abra powersheel como admin e usa este código
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
_____________________________________________________________________________

#ativa máquina virtual
.\env\Scripts\Activate\.bat
_____________________________________________________________________________

#instalando django
 pip install django
_____________________________________________________________________________

#cria super usuário
python manage.py createsuperuser
_____________________________________________________________________________

#cria models
python manage.py makemigrations
_____________________________________________________________________________

#cria tabelas no banco de dados
python manage.py migrate
_____________________________________________________________________________

#iniciando projeto
python manage.py runserver
_____________________________________________________________________________
