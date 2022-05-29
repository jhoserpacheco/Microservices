# Microservicios
## _Development of web applications based on microservices subject - Second exam_ 

The adminsitration of the BECL (Biblioteca Eduardo Cote Lemus) require of an app to
manage the entrance, and out of the alumns. The principal reason to achieve that is
for get the data registers and the administration know about the behavior of the BECL

## This project has createad by:

- @jhoserpacheco
- @yadirGarcia
- @robeedbenitez
- @JavierDeluxe

## INSTALLATION

### Clone repository use

``git clone https://github.com/jhoserpacheco/Microservices``

#### Change directory and Activate Environment
``cd MICROSERVICES``
``python -m venv env``
``. env/bin/activate``

#### Install requirements.txt and make migrations 
``pip install -r requirements.txt``
``python manage.py makemigrations``
``python manage.py migrate``

#### Run server 
``python manage.py runserver``

<hr>

## VARIABLES ENVIRONMENTS 

#### Create file '.env' with:
* CLIENTE_ID=ID_CLIENT_GOOGLE_API
* SECRET=SECRET_CLIENT_GOOGLE_API
* SECRET_KEY=DJANGO_SECRET_KEY 