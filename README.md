# cashback-verde-marketplace
# Iniciaremos instalando o django no ambiente virtual com
pip install django

# salvando as bibliotecas salvas no requirements

pip freeze > requirements.txt

# criando projeto django-admin

django-admin startproject retorno_natural

# iniciando a aplicação

django-admin startapp core

# Criando superusuario - admin_natural sW@-1;
python manage.py createsuperuser