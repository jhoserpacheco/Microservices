# ENTRANCE MICROSERVICE
<hr>

## INSTALLATION

### Clone repository use

```bash
git clone https://github.com/Microservices-BECL-UFPS/entrance-microservice.git
```

#### Change directory and Activate Environment
```bash
cd entrance-microservice
```

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

#### Install requirements.txt
```bash
pip install -r requirements.txt
```

## VARIABLES ENVIRONMENTS 

#### Create file '.env' with:
* REQUESTS_URL=http://127.0.0.1:<strong>{USER_MICROSERVICE_PORT}</strong>/
* VERIFY_URL=auth/api/v1/token/verify/
* SUBSCRIPTION_KEY=LEAVE_THIS_KEY_EMPTY
* SECRET_KEY=DJANGO_SECRET_KEY

<strong>Note:</strong> The variable 'SECRET_KEY' must be equals to that of the user microservice.

## RUN MIGRATIONS

```bash
python manage.py makemigrations entrance_app
```

```bash
python manage.py migrate
```

## RUN SERVER
```bash
python manage.py runserver
```
<br>

# ENDPOINTS

|ACTION|METHOD|SUFIX|REQUEST_BODY|RESPONSE_BODY|
|------|------|----|------|------|
|Obtain QR|POST|/entrance/api/v1/obtain_qr/|[Here](#request-body-obtain-qr)|[Here](#response-body-obtain-qr)
|Confirm Entrance|POST|/entrance/api/v1/confirm_entrance/|[Here](#request-body-confirm)|[Here](#response-body-confirm)
|Confirm Exit|POST|/entrance/api/v1/confirm_exit/|[Here](#request-body-confirm)|[Here](#response-body-confirm)


### Obtain QR ENTRANCE/EXIT Request and Response
#### Request body obtain qr:
```json
{
    "group_id": 1
}
```

#### Response body obtain qr:
```json
{
    "qrcode": "BASE_64_QR_CODE_IMAGE"
}
```

### Confirm Entrance / Exit Request and Response
#### Request body confirm:
```json
{
    "user_id": 2, 
    "key": "EXTRACT_FROM_QR_CODE"
}
```

#### Response body confirm:
```
status: 200 OK
```
Note: Both the entrance and exit are equals in the request body and response body <strong>BUT</strong> the key is different.
<br>
Summary, the user must generate a qr code for entrance and another qr for exit.
